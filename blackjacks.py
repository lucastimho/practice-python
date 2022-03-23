import random


class Deck():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = ["two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "jack", "queen", "king", "ace"]

    def __init__(self):
        pass

    def hit(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method.")

    def hold(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method.")


class Dealer(Deck):
    rand1 = random.randint(0, 12)
    rand2 = random.randint(0, 12)

    def __init__(self):
        self.down = Deck.deck[Dealer.rand1]
        self.downname = Deck.card[Dealer.rand1]
        self.up = Deck.deck[Dealer.rand2]
        self.upname = Deck.card[Dealer.rand2]
        self.hand = self.down + self.up

    def display(self):
        print("Dealer's hand contains a(n) " + self.upname + ".")

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(0, 12)]
        print("Dealer has " + str(self.hand) + ".")

    def hold(self):
        print("Dealer will stand at " + str(self.hand) + ".")


class Player(Deck):
    rand1 = random.randint(0, 12)
    rand2 = random.randint(0, 12)

    def __init__(self, balance):
        self.card1 = Deck.deck[Player.rand1]
        self.card1name = Deck.card[Player.rand1]
        self.card2 = Deck.deck[Player.rand2]
        self.card2name = Deck.card[Player.rand2]
        self.hand = self.card1 + self.card2
        self.balance = balance

    def display(self):
        print("Your hand has a(n) " + self.card1name +
              " and a(n) " + self.card2name + ".")

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(0, 12)]
        print("Player has " + str(self.hand) + ".")

    def hold(self):
        print("Player will stand at " + str(self.hand) + ".")

    def wager(self, bet):
        self.bet = bet


dealer = Dealer()
player = Player(300)
dealer.display()
player.display()
