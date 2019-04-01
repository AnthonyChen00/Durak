import sys
import socket
import selectors
import types

class Server:
    def __init__(self):
        """Contructor for game server"""
        server_addr = ('127.0.0.1','65432')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(sever_addr)
        self.socket.listen()
        self.sel = selectors.DefaultSelector()
        self.numPlayers = 2
        self.currentPlayers = 0

    def acceptPlayer(self,socket):
        """Accept and register players"""
        conn, addr = socket.accept()
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb = b"", outb = b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn,events,data=data)
        self.currentPlayers += 1

    def serviceConnection(self,key,mask):
        sock = key.fileobj
        data = key.data
        if self.currentPlayers != self.numPlayers:
            print("Waiting for other players")
        else:
            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(1024)
                if recv_data:
                    data.outb += recv_data
                else:
                    print("closing connection to ", data.addr)
                    self.sel.unregister(sock)
                    sock.close()
            if mask & selectors.EVENT_WRITE:
                if data.outb:
                    print("Echoing data...")

if __name__ == '__main__':
    print("Initializing Server")
    gameServer = Server()
    gameServer.sel.register(gameServer.socket,selectors.EVENT_READ, data=None)
    gameServer.socket.setblocking(False)
    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None: #if there is no data then accept the player
                    gameServer.acceptPlayer(key.fileobj)
                else:
                    gameServer.serviceConnection(key,mask)
    except KeyboardInterrupt:
        print("KeyboardInterrupt read, closing server")
    finally:
        sel.close()
