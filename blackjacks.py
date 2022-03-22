import random


class Deck():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = ["one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "jack", "queen", "king", "ace"]

    def __init__(self):
        pass


class Dealer(Deck):
    def __init__(self):
        rand1 = random.randint(0, 13)
        self.down = Deck.deck[rand1]
        self.downname = Deck.card[rand1]
        rand2 = random.randint(0, 13)
        self.up = Deck.deck[rand2]
        self.upname = Deck.card[rand2]


dealer = Dealer()
print(dealer.down)
print(dealer.downname)
