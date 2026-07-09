class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def debit(self, amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
            print(f"Debited {amount}.\n New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}.\n New balance: {self.balance}")

cust1 = Account(1000, "123456789")
cust1.debit(eval(input('Enter amount you want to withdraw: ')))
cust1.credit(eval(input('Enter amount you want to deposit: ')))
