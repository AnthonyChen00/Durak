class GameState:
    def __init__(self):
        self.deck = []
        self.numPlayers = 2
        self.attacker = 0
        self.defender = 1


    def rules(self):
        """Used to print out the rules of the games, will be used to set up the game"""
        prompt = ""
        while prompt != "n":
            print("============================================================")
            print("Every card has a unique index 0 - 51...")
            print("inputs will ask for the unique card index")
            print("for example: 0 - | 1 ♥ |, the one of Hearts has an id of 0")
            prompt = input("Do you wish to repeat? (y/n): ")

        prompt = ""
        while prompt != "n":
            print("============================================================")
            print("Two players: 1 attacker and 1 defender")
            print("Attackers select a card from hand, may attack with multiple")
            print("of the same rank")
            print("Defender must block with a higher ranking card or a card of trump suit")
            print("If defender is successful, the positions are swapped")
            print("If defender is unsuccessful, the attacker may attack again")
            prompt = input("Do you wish to repeat? (y/n): ")

        return 0

    def setupDeck(self):
        """Initialize a list that represent deck of 52 cards with indexs 0 - 51"""
        deck = []
        for i in range(52):
            deck.append(i)
        return deck

    def run_game(self):
        print(r"""
        .------..------..------..------..------.
        |D.--. ||U.--. ||R.--. ||A.--. ||K.--. |
        | :/\: || (\/) || :(): || (\/) || :/\: |
        | (__) || :\/: || ()() || :\/: || :\/: |
        | '--'D|| '--'U|| '--'R|| '--'A|| '--'K|
        `------'`------'`------'`------'`------'
                """)
        print("Text version of the Traditional Russian Card Game, Durak")
        print("Current version: 2 player")
        prompt = ""
        while prompt != 'y' and prompt != 'n':
            prompt = input("Do you wish to read the rules? (y/n): ")
        if prompt == 'y':
            self.rules()
        print("\n\n\n\n\n")
        print("====================Initializing deck========================")
        print("")
        self.deck = self.setupDeck()
