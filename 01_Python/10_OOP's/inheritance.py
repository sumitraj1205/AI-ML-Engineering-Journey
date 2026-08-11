class balance:
    def __init__(self,balance):
        self.balance = balance
class withdraw(balance):
    def withdraw(self):
        print(self.balance)
a = withdraw(10000)
a.withdraw()
