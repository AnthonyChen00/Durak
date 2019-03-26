import player as pl
import card as cardManager


"""testing player functions"""
test1 = pl.Player()
test2 = pl.Player()
for i in range (3):
    test1.addHand(3 + 13*i)
    test2.addHand(2 + 10*i)


# test1.printHand()
attackHand = test1.attack()
# # print("Attacking with: ", end=" ")
# cardManager.printNon(attackHand)
print("--")
print("NEXT TURN")
print("--")
test2.defend(attackHand)
"""########==========#########"""

"""testing card functions """
# tempHand = []
# for i in range(9,15):
#     tempHand.append(i)
#
# cardManager.printHand(tempHand)
#

# print(cardManager.compare(0,12))
