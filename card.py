#need to import gamestate, figure out the trump suit

"""Manages Card interactions"""
card_suit_symbol = {0:"♥", 1:"♣", 2:"♠", 3:"♦"}
card_rank_appearance = {0:"1",1:'2',2:'3',3:"4",4:'5',5:'6',6:"7",7:'8',8:'9',9:"J",10:'Q',11:'K',12:"A"}

#translate index into card values
def translateCards(index):
    """Takes index and returns a dictionary containing the rank and suit of card"""
    card = {'index':0,'rank':0,'suit':0, 'symbol_suit':'','symbol_rank':''}
    suit = 0
    card['index'] = index
    while(index >= 13):
        suit += 1
        index -= 13
    card['rank'] = index
    card['suit'] = suit
    card['symbol_suit'] = card_suit_symbol[suit]
    card['symbol_rank'] = card_rank_appearance[index]
    return card
#Card comparison - if a is larger than b

def compare(cardA,cardB):
    """return if cardA is higher rank than cardB"""
    card1 = translateCards(cardA)
    card2 = translateCards(cardB)
    trumpSuit = 0 # temp: need to implement trump suit
    # check if both are same suit - handles trump suit case
    if card1['suit'] == card2['suit']:
        if card1['rank'] > card2['rank']:
            return True
        else:
            return False
    # check if cardA is trumpsuit or higher rank
    else:
        if card1['rank'] > card2['rank'] or card1['suit'] == trumpSuit:
            return True
        else:
            return False

# printing from list

def printHand(list):
    """Printing out current hand in a row,"""
    for index in list: #temp: need add class of cards
        card = translateCards(index)
        print("{:2d} - | {:s} {:s} |".format(card['index'],card['symbol_rank'],card['symbol_suit']),end='\n')

def printNon(list):
    for index in list:
        card = translateCards(index)
        print("| {:s} {:s} |".format(card['symbol_rank'],card['symbol_suit']),end=' ')
    print("")
