import player as pl
import card as cardManager
import gamestate as GS

"""testing player functions"""
# test1 = pl.Player()
# test2 = pl.Player()
# for i in range (3):
#     test1.addHand(3 + 13*i)
#     test2.addHand(4 + 13*i)
#
#
# # test1.printHand()
# attackHand = test1.attack()
# # # print("Attacking with: ", end=" ")
# # cardManager.printNon(attackHand)
# print("--")
# print("NEXT TURN")
# print("--")
# print(test2.defend(attackHand))
# print("Current hand of test2: ", end = " ")
# cardManager.printNon(test2.currentHand)
"""########==========#########"""

"""testing card functions """
# tempHand = []
# for i in range(9,15):
#     tempHand.append(i)
#
# cardManager.printHand(tempHand)
#

# print(cardManager.compare(0,12))

"""########==========#########"""
"""Testing game states"""
game = GS.GameState()
game.run_game()
