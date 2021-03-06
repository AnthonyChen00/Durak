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
    trumpSuit = 5 # temp: need to implement trump suit; read trump suit from a setting files?
    if card1['rank'] == card2['rank']:
        return 'evaded'
    if card1['suit'] == card2['suit']:
        if card1['rank'] > card2['rank']:
            return True
        else:
            return False
    else:
        if card1['suit'] == trumpSuit:
            return True
        else:
            return False

def translateRanks(list):
    output = []
    for card in list:
        temp = translateCards(card)
        output.append(temp['rank'])
    return output

def check(currentHand, discardPile):
    """Check if player is able to attack with additional same rank cards
    return the valid cards that may be attacked with"""
    playableCards = []
    discardRanks = translateRanks(discardPile)
    for card in range(len(currentHand)):
        if (translateCards(currentHand[card]))['rank'] in discardRanks:
            playableCards.append(currentHand[card])
    return playableCards

## need to implement method of checking defense hand and cards going to be played

def printSymbol(index):
    return(card_suit_symbol[index])

def translateMsg(list):
    final = []
    for char in list:
        final.append(int(char))
    return final

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
