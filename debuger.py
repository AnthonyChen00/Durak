import player as pl
import card as cardManager


"""testing player functions"""
test1 = pl.Player()
for i in range (3):
    test1.addHand(3 + 13*i)

# test1.printHand()
attackHand = test1.attack()
print("Attacking with: ", end=" ")
cardManager.printNon(attackHand)
# test1.defend([6,7,8])
"""########==========#########"""

"""testing card functions """
# tempHand = []
# for i in range(9,15):
#     tempHand.append(i)
#
# cardManager.printHand(tempHand)
#

# print(cardManager.compare(0,12))
