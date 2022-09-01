class Category:
    def __init__(self,account,balance=0) :
        self.account = account
        self.ledger =list()
        self.balance = balance
    def deposit(self,amount=0,description=''):
        self.ledger.append({"amount":amount,"description":description})
        self.balance += amount
        print(f"Your current balabce is {self.balance}$")
    
    def withdraw(self,amount=0,description=''):
        if amount > self.balance:
            print("Insufficient balance")
            return False
        else:
            self.ledger.append({"amount":-amount,"description":description})
            self.balance -= amount
            print(f"You have withdrawed {amount}$ you still have {self.balance}$ in the {self.account} account")
            return True
    def get_balance(self):
        print('\n'.join(([str(x["amount"]) for x in self.ledger])),'\n',self.balance)
        return self.balance
    def check_funds(self,amount):
        self.amount = amount
        if amount <= self.balance:
            return True
        return False
