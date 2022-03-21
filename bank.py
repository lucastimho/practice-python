class Bank():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        print("Owner: " + self.owner)
        self.balance = self.balance + deposit
        print("Balance: $" + str(self.balance))

    def withdraw(self, withdraw):
        if withdraw < self.balance:
            self.balance = self.balance - withdraw
            print("Your remaining balance is $" + str(self.balance) + ".")
        else:
            print("You do not have enough remaining balance to withdraw that amount.")


jose = Bank("Jose", 400)
print(jose.owner)
print(jose.balance)
jose.deposit(1200)
jose.withdraw(200)
jose.withdraw(5000)
