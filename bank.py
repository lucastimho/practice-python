class Bank():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


jose = Bank("Jose", 400)
print(jose.owner)
print(jose.balance)
