class bankaccount:
        def __init__(self, account_no, owner_name, balance):
            self.account_no = account_no
            self.owner_name = owner_name
            self.__balance = balance
        def deposit(self,amount):
            self.__balance  = self.__balance + amount
            print('new balance =',self.__balance )
        def withdraw(self,amount):
            if amount > self.__balance:
                  print("no money  to withdraw")
            else:
                 self.__balance = self.__balance - amount
                 print("you have withdrawn-",amount)
                 print("balance-",self.__balance)
        def check_balance(self):
             print("balance-",self.__balance)
        def transfer(self, amount, other_account):
            if amount > self.__balance:
                  print("no money  to withdraw")
            else:
                self.__balance = self.__balance - amount
                other_account.__balance = other_account.__balance + amount
                print("transfer done")
a = bankaccount(12345,"sumit raj",100000)
b = bankaccount(12347,"kunal jha2",0)
c = bankaccount(12346,"ravi raj",100)
a.deposit(10000)
b.withdraw(10)
c.check_balance()
a.transfer(1000, b)
b.check_balance()
print(c.account_no)

            