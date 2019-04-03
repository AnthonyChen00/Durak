import sys
import socket
import selectors
import types
from player import Player
import card as cardManager

class Client:
    def __init__(self,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sel = selectors.DefaultSelector()
        self.port = port
        self.player = Player(self.socket)

    def messageParse(self,msg):
        """Packet parser"""
        if msg[0] == 't':
            self.player.trump = int(msg[1:])
            print("trump suit is",self.player.trump)
        if msg[0] == 'd':
            msg = msg[2:].split("|")
            msg = cardManager.translateMsg(msg)
            print("Current Hand:")
            cardManager.printNon(msg)


    def startConnection(self):
        server_addr = ('127.0.0.1',int(self.port))
        self.socket.connect_ex(server_addr)
        self.socket.setblocking(False)

        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid = 0,
            outb=b"",
        )
        self.sel.register(self.socket, events, data=data)

    def serviceConnection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                self.messageParse(recv_data.decode("utf-8")) # packet parser


            # if not recv_data or data.recv_total == data.msg_total:
            #     print("Closing connection")
            #     self.sel.unregister(sock)
            #     sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(repr(data.outb))
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]

if __name__ == '__main__':
    print("Initializing Client")
    gameClient = Client(sys.argv[1])
    gameClient.startConnection()
    # try:
    while True:
        events = gameClient.sel.select(timeout=1)
        if events:
            for key, mask in events:
                gameClient.serviceConnection(key,mask)
        if not gameClient.sel.get_map():
            break
    # except KeyboardInterrupt:
    #     print("caught keyboard interrupt, exiting")
    # finally:
    gameClient.sel.close()
