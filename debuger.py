import player as pl

test1 = pl.Player()
for i in range (3):
    test1.addHand(3 + 13*i)

# test1.printHand()
test1.attack()
test1.defend([6,7,8])
