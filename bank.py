class Bank():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        print("Owner: " + self.owner)
        self.balance = self.balance + deposit
        print("Balance: $" + str(self.balance))


jose = Bank("Jose", 400)
print(jose.owner)
print(jose.balance)
jose.deposit(1200)
