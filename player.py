import random as rand
from error import Error

card_rank = {0:"1",1:'2',2:'3',3:"4",4:'5',5:'6',6:"7",7:'8',8:'9',9:"10",10:'11',11:'12',12:"A",13:"1",14:'2',15:'3',16:"4",17:'5',18:'6',19:"7",20:'8',21:'9',22:"10",23:'11',24:'12',25:"A",26:"1",27:'2',28:'3',29:"4",30:'5',31:'6',32:"7",33:'8',34:'9',35:"10",36:'11',37:'12',38:"A",39:"1",40:'2',41:'3',42:"4",43:'5',44:'6',45:"7",46:'8',47:'9',48:"10",49:'11',50:'12',51:"A"}

card_suit_symbol = {0:"♥",1:'♥',2:'♥',3:"♥",4:'♥',5:'♥',6:"♥",7:'♥',8:'♥',9:"♥",10:'♥',11:'♥',12:"♥",13:"♣",14:'♣',15:'♣',16:"♣",17:'♣',18:'♣',19:"♣",20:'♣',21:'♣',22:"♣",23:'♣',24:'♣',25:"♣",26:"♠",27:'♠',28:'♠',29:"♠",30:'♠',31:'♠',32:"♠",33:'♠',34:'♠',35:"♠",36:'♠',37:'♠',38:"♠",39:"♦",40:'♦',41:'♦',42:"♦",43:'♦',44:'♦',45:"♦",46:'♦',47:'♦',48:"♦",49:'♦',50:'♦',51:"♦"}

card_suit = {0:"0",1:'0',2:'0',3:"0",4:'0',5:'0',6:"0",7:'0',8:'0',9:"0",10:'0',11:'0',12:"0",13:"1",14:'1',15:'1',16:"1",17:'1',18:'1',19:"1",20:'1',21:'1',22:"1",23:'1',24:'1',25:"1",26:"2",27:'2',28:'2',29:"2",30:'2',31:'2',32:"2",33:'2',34:'2',35:"2",36:'2',37:'2',38:"3",39:"3",40:'3',41:'3',42:"3",43:'3',44:'3',45:"3",46:'3',47:'3',48:"3",49:'3',50:'3',51:"3"}

class Player:
    def __init__(self):
        """Constructor for player"""
        self.playerid = 0 # player id for attack/defend
        self.currentHand = [] # store current cards in hand
        self.AI = False # future implementations of AI Control
        self.currentAttacks = [] # temp: store the total current attacks for group attacks
        self.trump = 0;

    def sendRequest(self,socket):
        """User/client send a request to host, will return the player id"""
        self.playerid = socket # temp: will update for socket programming

    def printHand(self,list):
        """Printing out current hand in a row,"""
        for card in list: #temp: need add class of cards
            print("{:d} - | {:s} {:s} |".format(card,card_rank[card],card_suit_symbol[card]))

        print("===============")

    def addHand(self,newCard):
        """Adds a card into players hand - used for the drawing functions"""
        """newCard currently accepted as int, will change to card class"""
        if type(newCard) == int: #temp: need to change into class cards
            self.currentHand.append(newCard)
        else:
            Error("newCard incorrect type")

    def attack(self): # need to check defenders handcount
        """Select a card from player's current hand and returns it"""
        """Always returns a list of values"""
        if self.AI:
            # return rand.randint(0,len(self.currentHand))
            Error("AI not yet implemented for Attacking")
        else:
            print("Select card from... ")
            self.printHand(self.currentHand)
            card = int(input())
            while card not in self.currentHand: # error checking
                print("Please select a valid card from...", end = " ")
                self.printHand(self.currentHand)
                card = int(input())
            card = self.checkDoubles(card)
            return card

    def checkDoubles(self,card): # need to check defenders handcount...
        """Attack helper function if attacker's hand contains multiple of same rank"""
        multipleCards = [card]
        for i in range(4): # checking all other possible cards of same rank
            card_plus = card + 13 * i # checking higher values
            card_minus = card - 13 * i # checking lower values
            if card_plus in self.currentHand and card_plus < 51 and card_plus != card and card_plus not in multipleCards:
                prompt = input("Do you wish to add: {:d} - | {:s} {:s} | ? (y/n)".format(card_plus,card_rank[card_plus],card_suit_symbol[card_plus]))
                while prompt != 'y' and prompt != 'n': # input checking
                    prompt = input("Do you wish to add: {:d} - | {:s} {:s} | ? (y/n)".format(card_plus,card_rank[card_plus],card_suit_symbol[card_plus]))
                if prompt == 'y':
                    print("added")
                    multipleCards.append(card_plus)
                else:
                    print("Did not add")
            if card_minus in self.currentHand and card_minus > 0 and card_plus != card and card_minus not in multipleCards:
                prompt = input("Do you wish to add: {:d} - | {:s} {:s} | ? (y/n)".format(card_minus,card_rank[card_minus],card_suit_symbol[card_minus]))
                while prompt != 'y' and prompt != 'n': # input checking
                    prompt = input("Do you wish to add: {:d} - | {:s} {:s} | ? (y/n)".format(card_minus,card_rank[card_minus],card_suit_symbol[card_minus]))
                if prompt == 'y':
                    print("added")
                    multipleCards.append(card_minus)
                else:
                    print("Did not add")
        return multipleCards

    def defend(self,targets):
        """Will handle the entire players defend phase, inputs is all the cards being attacked with
        and the defender must handle all of them"""
        """Accept targets as a list"""
        if len(self.currentHand) < len(targets): #Goes against the rules of the game
            Error("Incorrect amount of targets")
        defendStatus = False
        if self.AI:
            Error("AI not yet implemented for defending")
        else:
            print("Cards that are currently attacking P" + str(self.playerid) + ":")
            self.printHand(targets)
            print("Cards in your hand")
            self.printHand(self.currentHand)
            for attacker in targets: # iterate thru all attackers
                defendCard = int(input("which card do you want to defend with from {:d} - | {:s} {:s} |?".format(attacker,card_rank[attacker],card_suit_symbol[attacker])))
                while defendCard not in self.currentHand: # input checking
                    defendCard = int(input("which card do you want to defend with?"))
                # check if defenderCard is larger
                # if not, ask if defender wants to give up or choose larger card

        return defendStatus
