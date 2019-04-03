import sys
import socket
import selectors
import types
import card as cardManager
from player import Player
from gamestate import GameState
import random

class Server:
    def __init__(self,port):
        """Contructor for game server"""
        server_addr = ('127.0.0.1',port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1',int(port)))
        self.socket.listen()
        self.game = GameState()
        self.sel = selectors.DefaultSelector()
        self.numPlayers = 2
        self.currentPlayers = 0
        self.players = []

    def acceptPlayer(self,socket):
        """Accept and register players"""
        conn, addr = socket.accept()
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb = b"", outb = b"")
        ####Selector
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn,events,data=data)
        ###gamestate manager
        self.currentPlayers += 1
        newPlayer = Player(conn)
        self.players.append(newPlayer) #for socket
        self.game.addPlayer(newPlayer) #for game functions
        #
        print("Current numbers of connections:", self.currentPlayers)
        if self.currentPlayers == self.numPlayers:
            #begin the turn based
            for player in self.players:
                #send to all players
                player.conn.send(b"Starting Game...")
            self.startGame()
    # def sendAll(self,msg):
    #     """Send a message to all players"""

    def startGame(self):
        """Initialize the deck, trump suit, and player order"""
        #player order is determined by join order, the first player is attacker
        print("Starting deck")
        self.game.setupDeck()
        playerHands = self.game.createHand()
        trump = "t"+str(random.randint(0,3))
        for i in range(len(self.players)):
            playerHand = "d"
            for j in playerHands[i]:
                playerHand += "|"
                playerHand += str(j)
            self.players[i].conn.send(playerHand.encode("utf-8"))



    def serviceConnection(self,key,mask):
        """Handle the messages from players"""
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print("closing connection to ", data.addr)
                print("Current numbers of connections:", self.currentPlayers)
                self.currentPlayers -= 1
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if self.currentPlayers == self.numPlayers:
                if data.outb:
                    print("Echoing data...")
                    #send to other players
                    for player in self.players:
                        if sock != player.conn:
                            sent = player.conn.send(data.outb)
                            data.outb = data.outb[sent:] #fundamental to end the sending process
            else:
                if data.outb:
                    data.outb = b"Waiting on more players..."
                    sent = sock.send(data.outb)
                    data.outb = data.outb[sent:]


if __name__ == '__main__':
    print("Initializing Server")
    gameServer = Server(sys.argv[1])
    gameServer.sel.register(gameServer.socket,selectors.EVENT_READ, data=None)
    gameServer.socket.setblocking(False)
    try:
        while True:
            events = gameServer.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None: #if there is no data then accept the player
                    gameServer.acceptPlayer(key.fileobj)
                else:
                    gameServer.serviceConnection(key,mask)
    except KeyboardInterrupt:
        print("KeyboardInterrupt read, closing server")
    finally:
        gameServer.sel.close()
        gameServer.socket.close()
