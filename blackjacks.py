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

    def __init__(self):
        self.down = Deck.deck[random.randint(0, 12)]
        self.downname = Deck.card[random.randint(0, 12)]
        self.up = Deck.deck[random.randint(0, 12)]
        self.upname = Deck.card[random.randint(0, 12)]
        self.hand = self.down + self.up

    def display(self):
        print("Dealer's hand contains a(n) " + self.upname + ".")

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(0, 12)]
        print("Dealer has " + str(self.hand) + ".")

    def hold(self):
        print("Dealer will stand at " + str(self.hand) + ".")


class Player(Deck):

    def __init__(self):
        self.card1 = Deck.deck[random.randint(0, 12)]
        self.card1name = Deck.card[random.randint(0, 12)]
        self.card2 = Deck.deck[random.randint(0, 12)]
        self.card2name = Deck.card[random.randint(0, 12)]
        self.hand = self.card1 + self.card2

    def display(self):
        print("Your hand has a(n) " + self.card1name +
              " and a(n) " + self.card2name + ".")

    def balance(self, balance):
        self.balance = balance

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(0, 12)]
        print("Player has " + str(self.hand) + ".")

    def hold(self):
        print("Player will stand at " + str(self.hand) + ".")

    def wager(self, bet):
        self.bet = bet
        self.balance = self.balance - self.bet


def game():
    dealer = Dealer()
    player = Player()

    dealer.display()
    player.display()


cont = True
while cont:
    game()
    play = input("Would you like to play again? (y/n)")
    if str(play) == "n":
        cont = False
