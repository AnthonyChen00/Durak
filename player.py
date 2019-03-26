import random as rand
from error import Error
import card as cardManager

class Player:
    def __init__(self):
        """Constructor for player"""
        self.playerid = 0 # player id for attack/defend
        self.currentHand = [] # store current cards in hand
        self.AI = False # future implementations of AI Control
        self.currentAttacks = [] # temp: store the total current attacks for group attacks

    def sendRequest(self,socket):
        """User/client send a request to host, will return the player id"""
        self.playerid = socket # temp: will update for socket programming


    def addHand(self,newCard):
        """Adds a card into players hand - used for the drawing functions"""
        """newCard currently accepted as int, will change to card class"""
        if type(newCard) == int:
            if newCard < 0 or newCard > 51:
                Error("Attempt to add card out of range")
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
            cardManager.printHand(self.currentHand)
            card = int(input("to your attack: "))
            while card not in self.currentHand: # error checking
                print("Please select a valid card from...", end = " ")
                cardManager.printHand(self.currentHand)
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
                print("Do you wish to add:")
                cardManager.printHand([card_plus])
                prompt= input("to your attack? (y/n):")
                while prompt != 'y' and prompt != 'n': # input checking
                    print("Do you wish to add:")
                    cardManager.printHand([card_plus])
                    prompt = input("to your attack? (y/n):")
                if prompt == 'y':
                    print("added")
                    multipleCards.append(card_plus)
                else:
                    print("Did not add")
            if card_minus in self.currentHand and card_minus > 0 and card_plus != card and card_minus not in multipleCards:
                prompt = input("Do you wish to add:")
                cardManager.printHand([card_minus])
                prompt = input("to your attack? (y/n):")
                while prompt != 'y' and prompt != 'n': # input checking
                    prompt = input("Do you wish to add:")
                    cardManager.printHand([card_minus])
                    prompt = input("to your attack? (y/n):")
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
        """Return list - discardCards (if 0 means defender accepts all the cards)"""
        if len(self.currentHand) < len(targets): #Goes against the rules of the game
            Error("Incorrect amount of targets")
        defendStatus = False
        discardCards = []
        forfeit = False
        if self.AI:
            Error("AI not yet implemented for defending")
        else:
            print("Cards that are currently attacking P" + str(self.playerid) + ":")
            cardManager.printNon(targets)
            print("Cards in P" + str(self.playerid) + " hand to defend with:")
            cardManager.printHand(self.currentHand)
            for attackCard in targets: # iterate thru all attackers
                validDefend = False
                while validDefend == False and forfeit == False:
                    print("which card do you want to defend with from:" , end=" ")
                    cardManager.printNon([attackCard])
                    defendCard = int(input())
                    while defendCard not in self.currentHand: # input checking
                        defendCard = int(input("which card do you want to defend with?"))
                    # check if defenderCard is larger/ choose new card or give up
                    validDefend = cardManager.compare(defendCard,attackCard)
                    if validDefend == False:
                        print("Failed defense...")
                        prompt = input("Do you wish to give up defense? (y/n)")
                        while prompt != "y" and prompt != 'n': # input checking
                            prompt = input("Do you wish to give up defense? (y/n)")
                        if prompt == 'y':
                            forfeit = True
                            print(forfeit)
                            break           
                if forfeit:
                    break
                # print("valid defend!")
                # self.currentHand.remove(defenderCard)
                # discardCards.append(defenderCard)
                # discardCards.append(attackCard)
                #
            #results handling:
        if forfeit:
            print("3 - GIVE UP!")


        return discardCards
