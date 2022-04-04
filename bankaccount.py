class BankAccount:

    def __init__(self, name, balance, int_rate):
        self.name = name
        self.amount = 0
        self.balance = balance
        self.int_rate = int_rate

    # @classmethod
    # def display_all():
    #     pass

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        if self.balance < amount:
            balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.int_rate * self.balance
        return self


josh = BankAccount("Josh", 500, 0.02)
rob = BankAccount("Rob", 800, 0.02)

josh.deposit(400).deposit(800).deposit(400).withdrawal(500).yield_interest().display_account_info()

rob.deposit(300).deposit(600).withdrawal(400).withdrawal(600).withdrawal(200).withdrawal(100).yield_interest().display_account_info()
