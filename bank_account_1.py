class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdrawing(self, withdraw):
        self.balance = self.balance - withdraw

    def deposit(self, deposit):
        self.balance = self.balance + deposit

    def current_balance(self):
        return self.balance


bank_account = BankAccount(50)
bank_account.withdrawing(10)
print(f"current_balance: {bank_account.current_balance()}")
bank_account.deposit(100)
print(f"current_balance: {bank_account.current_balance()}")
