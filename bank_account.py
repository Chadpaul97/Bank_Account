
class BankAccount:

    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_user_info(self):
        print("Balance:",self.balance)
        return self

    def yield_intrest(self):
        self.balance += self.balance*self.int_rate
        return self



upper_bank = BankAccount()
lower_bank = BankAccount()

upper_bank.deposit(300).deposit(300).deposit(300).withdraw(910).display_user_info()
lower_bank.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).display_user_info()
