class bank:
    def __init__(self,name,balance,id):
        self.name = name
        self.__balance = balance
        self._id = id
    def get_balance(self):
        print(self.__balance)
    def update(self,newbalance):
        self.__balance = newbalance
a= bank("sumit", 10_000,1205)
print(a.name)
print(a._id)
a.get_balance()
a.update(20000)