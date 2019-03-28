# Durak ('fool')
This is a loose interpretation of Durak with a deck of 52 cards and 4 players.
## Summary:
 [Durak](https://en.wikipedia.org/wiki/Durak) is a traditional Russian card game that is popular in many post- Soviet states. It is Russia's most popular card. The main objective is to shed all one's cards when there are no more cards left in the deck. At the end of the game, the last player with cards in their hand is the durak or 'fool'.
## Rules:
### Setup:
A card game played with 2 - 5 players, using a deck of 52 cards. The deck is shuffled and each player is dealt 6 cards. The bottom of the deck will be flipped up to determine the trump suit of the current round. For example, if it was the Six of diamonds, then diamonds are a higher rank than all plain-suit cards. The rest of the deck will remain face-down and serve as the deck for players to draw from. Another pile will be the discard pile of the used cards.
The Ace is the highest rank card of each suit and the Two is the lowest rank card of each suit. A trump card of any rank beats all cards in the other suits. For example, a Six of trumps beats an Ace of any other suit.
### Playing:
The player with the lowest trump is the first attacker and leads the first attack. The player to the attacker's left is always the defender. After each round of attack play proceeds clockwise. If the attacker succeeds, the defender loses their turn and the attack passes to the player on the defender's left. If the attack fails, the defend becomes the next attacker.
#### Attack
The attacker opens their turn by playing a card face up on the table as an attacking card. The player to the attacker's left is the defender. They respond to the attack with a defending card.

Other players may increase the attack by adding cards of the same rank of any card (attacking or defending) to the attack.
For example: attacker attacks with 4 of Hearts
* Other players besides the defender may contribute additional with 4 of other suits to the attack.
* Defender blocks attack the attack with a higher rank of Hearts, for example 6 of Hearts. All other players may contribute to the attack with  6 of other suits.

**NOTE:** There may not be a higher number of cards in the attack compared to the number of cards in the hand of the defender. For example, if the defender has 4 cards in their hand, the maximum number of cards in the attack is 4 cards.
#### Defend
The defender attempts to beat the attack card by playing a higher-ranking defending card from their hand. For example, if the attacker plays an 8 of Spades the defender must play a higher Spades such as the 10 of Spades or a card from the trump suit to defend successfully.  However all other players may increase the attack with cards played by the defender (refer to attack section).

**NOTE:** Defender has to successfully block all cards or else they take all the cards of the attack into their hand

**NOTE** Defender may play a card of the same rank to "deflect" the initial attack and shift the attack into the next player.

## [Current Progress](https://trello.com/b/8bwXfL5C/personal-ideas):
Checkmark  | Goal
--- | -----------------------
Done | Rough block diagram of game loop
WIP| text based prototype of logic
o | Implement basic window/application, base classes
o | Socket Programming: creating a host and client programs and perspective communication
o | UI, maybe a menu screen(?)
o | animations??? - super unlikely
o | AI???? - super unlikely

### Block diagram of game
![:)](https://github.com/AnthonyChen00/Durak/blob/master/assets/workflow.png)

### Small example of text based prototype
Current examples of code:
* Attacking and Defending
* Introduction & rules

>python3 debuger.py

```

        .------..------..------..------..------.
        |D.--. ||U.--. ||R.--. ||A.--. ||K.--. |
        | :/\: || (\/) || :(): || (\/) || :/\: |
        | (__) || :\/: || ()() || :\/: || :\/: |
        | '--'D|| '--'U|| '--'R|| '--'A|| '--'K|
        `------'`------'`------'`------'`------'

Text version of the Traditional Russian Card Game, Durak
Current version: 2 player
Do you wish to read the rules? (y/n): n






===================Initializing Game=======================

=======Player 0 turn=======
Select card from...
 1 - | 2 ♥ |
14 - | 2 ♣ |
 3 - | 4 ♥ |
26 - | 1 ♠ |
15 - | 3 ♣ |
40 - | 2 ♦ |
to your attack: 1
Do you wish to add:
14 - | 2 ♣ |
to your attack? (y/n):n
Did not add
Do you wish to add:
40 - | 2 ♦ |
to your attack? (y/n):n
Did not add
=======Player 1 turn=======
Cards that are currently attacking P1:
| 2 ♥ |
Cards in P1 hand to defend with:
13 - | 1 ♣ |
 2 - | 3 ♥ |
30 - | 5 ♠ |
16 - | 4 ♣ |
44 - | 6 ♦ |
38 - | A ♠ |
which card do you want to defend with from: | 2 ♥ |
4
which card do you want to defend with?5
which card do you want to defend with?2
valid defend!
=======Player 0 turn=======
Attack was blocked, Current avaiable attack-able cards:
| 2 ♣ | | 3 ♣ | | 2 ♦ |
Do you wish to continue your attack? (y/n)n
```
