#need to import gamestate, figure out the trump suit

"""Manages Card interactions"""
# card_rank = {0:"1",1:'2',2:'3',3:"4",4:'5',5:'6',6:"7",7:'8',8:'9',9:"10",10:'11',11:'12',12:"A",13:"1",14:'2',15:'3',16:"4",17:'5',18:'6',19:"7",20:'8',21:'9',22:"10",23:'11',24:'12',25:"A",26:"1",27:'2',28:'3',29:"4",30:'5',31:'6',32:"7",33:'8',34:'9',35:"10",36:'11',37:'12',38:"A",39:"1",40:'2',41:'3',42:"4",43:'5',44:'6',45:"7",46:'8',47:'9',48:"10",49:'11',50:'12',51:"A"}
#
# card_suit_symbol = {0:"♥",1:'♥',2:'♥',3:"♥",4:'♥',5:'♥',6:"♥",7:'♥',8:'♥',9:"♥",10:'♥',11:'♥',12:"♥",13:"♣",14:'♣',15:'♣',16:"♣",17:'♣',18:'♣',19:"♣",20:'♣',21:'♣',22:"♣",23:'♣',24:'♣',25:"♣",26:"♠",27:'♠',28:'♠',29:"♠",30:'♠',31:'♠',32:"♠",33:'♠',34:'♠',35:"♠",36:'♠',37:'♠',38:"♠",39:"♦",40:'♦',41:'♦',42:"♦",43:'♦',44:'♦',45:"♦",46:'♦',47:'♦',48:"♦",49:'♦',50:'♦',51:"♦"}
#
# card_suit = {0:"0",1:'0',2:'0',3:"0",4:'0',5:'0',6:"0",7:'0',8:'0',9:"0",10:'0',11:'0',12:"0",13:"1",14:'1',15:'1',16:"1",17:'1',18:'1',19:"1",20:'1',21:'1',22:"1",23:'1',24:'1',25:"1",26:"2",27:'2',28:'2',29:"2",30:'2',31:'2',32:"2",33:'2',34:'2',35:"2",36:'2',37:'2',38:"3",39:"3",40:'3',41:'3',42:"3",43:'3',44:'3',45:"3",46:'3',47:'3',48:"3",49:'3',50:'3',51:"3"}

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
    trumpSuit = 0
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
