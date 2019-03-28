import player as pl
import card as cardManager
import gamestate as GS

"""testing player functions"""
# test1 = pl.Player()
# test2 = pl.Player()
# for i in range (3):
#     test1.addHand(3 + 13*i)
#     test2.addHand(4 + 13*i)
# #
# attackCards = test1.attack()
# d

"""########==========#########"""

"""testing card functions """
# tempHand = []
# for i in range(9,15):
#     tempHand.append(i)
#
# cardManager.printHand(tempHand)
#

# print(cardManager.compare(0,12))
# cardManager.printNon([27,28,29])
# cardManager.printNon([14,15,16])
# print(cardManager.check([27,28,29],[14,15,16]))

"""########==========#########"""
"""Testing game states"""
game = GS.GameState()
game.run_game()
