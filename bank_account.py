class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        print('__init__', balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('deposit', amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print('withdraw', amount)

    def print_amount(self):
        print(f"account balance: {self.balance}")

kates_account = BankAccount(7)
kates_account.print_amount()
kates_account.deposit(10)
kates_account.print_amount()
kates_account.withdraw(5)
kates_account.print_amount()
