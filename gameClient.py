import sys
import socket
import selectors
import types

messages = [b"Message 1 from client", b"Message 2 from client."]

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(False)
        self.sel = selectors.DefaultSelector()
        # self.playerID = 0
        # self.AI = False
        # self.currentHand = []

    def startConnection(self):
        server_addr = ('127.0.0.1','65432')
        self.socket.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid = 0
            msg_total=sum(len(m)for m in messages)
            recv_total = 0
            messages = list(messages)
            outb=b""
        )
        self.sel.register(self.socket, events, data=data)

    def serviceConnection(key,mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                print("recieved", repr(recv_data), "from connection", data.connid)
                data.recv_total += len(recv_data)
            if not recv_data or data.recv_total == data_msg_total:
                print("Closing connection")
