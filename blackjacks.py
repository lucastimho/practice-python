import random


class Deck():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = ["one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "jack", "queen", "king", "ace"]

    def __init__(self):
        pass


class Dealer(Deck):
    rand1 = random.randint(0, 13)
    rand2 = random.randint(0, 13)

    def __init__(self):
        self.down = Deck.deck[Dealer.rand1]
        self.downname = Deck.card[Dealer.rand1]
        self.up = Deck.deck[Dealer.rand2]
        self.upname = Deck.card[Dealer.rand2]


class Player(Deck):
    rand1 = random.randint(0, 13)
    rand2 = random.randint(0, 13)

    def __init__(self):
        self.card1 = Deck.deck[Player.rand1]
        self.card2 = Deck.deck[Player.rand2]


dealer = Dealer()
print(dealer.down)
print(dealer.downname)
