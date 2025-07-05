#Q. Create a class BankAccount with deposite,withdraw and balance check methods

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposite(self,amount):
        self.balance +=amount
        print(f"deposite: Rs.{amount}")
    
    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance -= amount
            print(f"withdraw : Rs.{amount}")
        else:
            print("Insufficent balance")
    
    def show_balance(self):
        print(f"Balance: Rs.{self.balance}")

acc=BankAccount("Rahul")
acc.deposite(1000)
acc.withdraw(500)
acc.show_balance()