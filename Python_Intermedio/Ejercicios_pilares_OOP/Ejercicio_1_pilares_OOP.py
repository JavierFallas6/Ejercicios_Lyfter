class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Balance is below minimum balance accepted.")
        
        self.balance -= amount

account = SavingsAccount(1000, 500)

account.deposit(200)
print(account.balance) 

account.withdraw(800)
print(account.balance)
