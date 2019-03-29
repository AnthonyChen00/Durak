import random
from player import Player
import card as cardManager
from error import Error

class GameState:
    def __init__(self):
        self.deck = [] # contains card currently in deck
        self.players = [] # instances of players in game, used for attacking and defending; #FIFO format, 0 - attacker, 1 - defender
        self.trumpSuit = 0 # keep track of the trump suit throughout the game
        self.gameEnd = False


    def rules(self): #need to add settings?
        """Used to print out the rules of the games, will be used to set up the game"""
        prompt = ""
        while prompt != "n":
            print("======================Rules: Part 1========================")
            print("Every card has a unique index 0 - 51...")
            print("inputs will ask for the unique card index")
            print("for example: 0 - | 1 ♥ |, the one of Hearts has an id of 0")
            prompt = input("Do you wish to repeat? (y/n): ")

        prompt = ""
        while prompt != "n":
            print("======================Rules: Part 2========================")
            print("Two players: 1 attacker and 1 defender")
            print("Attackers select a card from hand, may attack with multiple")
            print("of the same rank")
            print("Defender must block with a higher ranking card or a card of trump suit")
            print("If defender is successful, the positions are swapped")
            print("If defender is unsuccessful, the attacker may attack again")
            prompt = input("Do you wish to repeat? (y/n): ")
        print("==========================The End==========================")
        return 0

    def nextTurn(self,skip): #need to account for unsuccessful block and defender loses turn
        """Shift the player buffer and return new attacker and new defender"""
        if skip == True:
            currentAttacker = self.players.pop(0)
            self.players.append(currentAttacker)
            return 0
        else:
            currentAttacker = self.players.pop(0)
            self.players.append(currentAttacker)
            currentAttacker = self.players.pop(0)
            self.players.append(currentAttacker)
            return 0

    def turn(self):
        """Performs the entire Active Phase"""
        activePhase = True
        discardPile = []
        attackCards = []
        defendStatus = True
        swapped = False
        while activePhase == True:
            # if pile is empty: first attack
            if len(discardPile) == 0:
                if swapped == False:
                    print("=======Player " + str(self.players[0].playerid) +" turn=======")
                    attackCards = self.players[0].attack()
                    # other players may join in attack
                    for i in range(2,len(self.players)):
                        validCards = cardManager.check(self.players[i].currentHand, attackCards)
                        if len(validCards) > 0:
                            print("=======Player " + str(self.players[i].playerid) +" turn=======")
                            print("Do you wish to add to the attack with: ")
                            cardManager.printNon(validCards)
                            prompt = ''
                            while prompt != 'y' and prompt != 'n':
                                prompt = input("Do you wish to continue your attack? (y/n)")
                            if prompt == 'y':
                                attackCards += (self.players[i].followUpAttack(validCards))

                # defender blocks
                print("=======Player " + str(self.players[1].playerid) +" turn=======")
                discardCards = self.players[1].defend(attackCards)
                # if defense is successful, attacker may attack again
                if len(discardCards) != 0:
                    if type(discardCards[0]) == str:
                        self.nextTurn(True)
                        self.printPlayerBuffer()
                        discardCards.pop(0)
                        attackCards = discardCards
                        print('Perfect Block')
                        swapped = True
                    else:
                        for card in range(len(discardCards)):
                            discardPile.append(discardCards[card])
                else:
                    activePhase = False
                    defendStatus = False
            else:
                # if attacker may attack with any card within the discardPile - need function of attacking based on discardPile
                # could add a checker if attacker can play additional cards...
                validCards = cardManager.check(self.players[0].currentHand, discardPile)
                if len(validCards) > 0:
                    print("=======Player " + str(self.players[0].playerid) +" turn=======")
                    print("Attack was blocked, Current avaiable attack-able cards: ")
                    cardManager.printNon(validCards)
                    prompt = input("Do you wish to continue your attack? (y/n)")
                    while prompt != 'y' and prompt != 'n':
                        prompt = input("Do you wish to continue your attack? (y/n)")
                    if prompt == 'n':
                        # ask other players
                        activePhase = False
                    else:
                        attackCards = self.players[0].followUpAttack(validCards)
                        ## other people attack as well
                        print("=======Player " + str(self.players[1].playerid) +" turn=======")
                        discardCards = self.players[1].followUpDefend(attackCards,discardPile)
                        if len(discardCards) != 0:
                            print(discardCards)
                            for card in range(len(discardCards)):
                                discardPile.append(discardCards[card])
                        else:
                            activePhase = False
                            defendStatus = False
                else:
                    activePhase = False
        # when redrawing, check size of deck
        for i in range(6):
            for player in self.players:
                if len(player.currentHand) < 6:
                    player.addHand(self.draw())

        return defendStatus


    def checkStatus(self): # have not confirm if it works
        """Check if the game is over"""
        #check the size of deck and cards in players hand
        if len(self.deck) == 0:
            for player in self.players:
                if len(player.currentHand)== 0:
                    print("Player P" + str(player.playerid) + "won!")
                    return True
        return False

    def setupDeck(self):
        """Initialize a list that represent deck of 52 cards with indexs 0 - 51"""
        deck = []
        for i in range(52):
            self.deck.append(i)
        self.trumpSuit = random.randint(0,3)
        # print("Trump Suit is: " + cardManager.printSymbol(self.trumpSuit)) // not implemented


    def draw(self):
        """Select a random card from current deck"""
        try:
            card = self.deck[random.randint(0,len(self.deck)-1)]
        except:
            Error("At Draw: ")
        self.deck.remove(card)
        return card

    def setupPlayer(self): #need to add more player support
        """Create the number of players in game, need to change for 4 players"""
        p1 = Player()
        p1.sendRequest(0)
        self.players.append(p1)
        p2 = Player()
        p2.sendRequest(1)
        self.players.append(p2)
        p3 = Player()
        p3.sendRequest(2)
        self.players.append(p3)
        p4 = Player()
        p4.sendRequest(3)
        self.players.append(p4)

    def printPlayerBuffer(self):
        print(self.players[0].playerid, self.players[1].playerid,self.players[2].playerid, self.players[3].playerid)


    def createHand(self):
        """Initialize players hands, draw up to 6 cards"""
        for i in range(6):
            for player in self.players:

    def printPlayersHands(self): # for debugging
        """Print current hand of all players"""
        for player in self.players:
            cardManager.printNon(player.currentHand)

    def run_game(self):
        """Main game loop, setup deck, initialize players, set trumpSuit, give player hands"""
        print(r"""
        .------..------..------..------..------.
        |D.--. ||U.--. ||R.--. ||A.--. ||K.--. |
        | :/\: || (\/) || :(): || (\/) || :/\: |
        | (__) || :\/: || ()() || :\/: || :\/: |
        | '--'D|| '--'U|| '--'R|| '--'A|| '--'K|
        `------'`------'`------'`------'`------'
                """)
        print("Text version of the Traditional Russian Card Game, Durak")
        print("Current version: 2 player")
        prompt = ""
        while prompt != 'y' and prompt != 'n':
            prompt = input("Do you wish to read the rules? (y/n): ")
        if prompt == 'y':
            self.rules()
        print("\n\n\n\n\n")
        print("===================Initializing Game=======================")
        print("")
        # initialize a fresh deck & # initialize the trump suit
        self.setupDeck()
        # initialize players & set playid - temp: need to add socket programming within this
        self.setupPlayer()
        # create each player's hand
        self.createHand()
        while self.gameEnd == False:
            defendStatus = self.turn()
            print("Defend Status: "+ str(defendStatus))
            self.printPlayerBuffer()
            print("++++++++++++++++++TURN OVER+++++++++++++++++++++++++++++")
            self.nextTurn(defendStatus)
            self.gameEnd = self.checkStatus()
