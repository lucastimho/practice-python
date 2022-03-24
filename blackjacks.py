import random


class Deck():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    # card = ["two", "three", "four", "five", "six", "seven",
    #         "eight", "nine", "ten", "jack", "queen", "king", "ace"]

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
        self.down = Deck.deck[random.randint(1, 13)]
        # self.downname = Deck.card[random.randint(0, 12)]
        self.up = Deck.deck[random.randint(1, 13)]
        # self.upname = Deck.card[random.randint(0, 12)]
        self.hand = self.down + self.up

    def display(self):
        print("Dealer's hand has at least a value of " + str(self.up) + ".")

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(1, 13)]
        print("Dealer has " + str(self.hand) + ".")

    def hold(self):
        print("Dealer will stand at " + str(self.hand) + ".")


class Player(Deck):

    def __init__(self):
        self.card1 = Deck.deck[random.randint(1, 13)]
        # self.card1name = Deck.card[random.randint(0, 12)]
        self.card2 = Deck.deck[random.randint(1, 13)]
        # self.card2name = Deck.card[random.randint(0, 12)]
        self.hand = self.card1 + self.card2

    def display(self):
        print("Your hand has " + str(self.card1 + self.card2) + ".")

    def balance(self, balance):
        self.balance = balance

    def hit(self):
        self.hand = self.hand + Deck.deck[random.randint(1, 13)]
        print("Player has " + str(self.hand) + ".")

    def hold(self):
        print("Player will stand at " + str(self.hand) + ".")

    def wager(self, bet):
        self.bet = bet
        self.balance = self.balance - self.bet


dealer = Dealer()
player = Player()


def convert_to_chips():
    money = True
    while money:
        balance = input("How much money would you like to put in to chips?")
        if balance.isdigit():
            player.balance(int(balance))
            money = False
        else:
            print("Please go back to elementary school to learn what numbers are.")


def game():
    print("Your balance is $" + str(player.balance) + ".")
    dealer.display()
    player.display()


def betting():
    money = True
    while money:
        wager = input("How much you want to wager?")
        if wager.isdigit() and int(wager) <= player.balance:
            player.wager(int(wager))
            responses = ["Ooh daring today aren't we?", "If you think you can handle that much.",
                         "Thanks (for the money)!", "When you going to start playing with the big boys?", "I've given my kid more money than that for chores.", "I don't condone taking kids' lunch money but I guess that changes now.", "Looks like another sucker I'm sending into debt."]
            print(responses[random.randint(0, 6)])
            money = False
        else:
            print("How about you put in a realistic number before I kick you out.")


def playing():
    if player.card1 + player.card2 == 21:
        print("BlackJack")
        player.balance = player.balance + player.wager * 2.5
    elif player.hand < 21:
        play = True
        while play:
            hit = input("Would you like to hit? (y/n)")
            if hit == "y":
                player.hit()


convert_to_chips()
cont = True
while cont:
    if player.balance > 0:
        betting()
    else:
        balance = input("Add more money to play.")
        if balance.isdigit():
            player.balance(int(balance))
        else:
            print("Okay we're done here.")
            break
    game()
    while cont:
        play = input("Would you like to play again? (y/n)")
        if str(play) == "n":
            print("Thanks for your money. Hope to see you again!")
            cont = False
        elif str(play) == "y":
            break
        else:
            print("Putting random letters is not going to get your money back.")
