# Bank account system

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} | New Balance: {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount} | New Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder} | Balance: {self.balance}")


# Running operations..
acc_1 = BankAccount("Alexis_101", 1000)
acc_1.deposit(500)
acc_1.withdraw(300)
acc_1.withdraw(1500)
acc_1.check_balance()
