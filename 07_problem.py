#Q. create a class Account with private balance.use getter and setter using @property.
class Account:
    def __init__(self):
        self.balance = 0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print("Invalid amount!")
        else:
            self._balance = amount

acc = Account()
acc.balance = 1000
print("Balance:",acc.balance)
acc.balance = 500