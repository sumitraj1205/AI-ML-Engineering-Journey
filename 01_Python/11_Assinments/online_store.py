class store:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        store.count += 1# it is the constructer so it will run only one time per class so it traces the no. of objects
    def get_info(self):
        print(f"the name of the poduct is {self.name} and price is{self.price}")
    def discount(self, discount):
        discount_rate = self.price*discount /100
        print("discount =",discount_rate)
    @classmethod
    def get_count(cls):#for counting no. of object created
        print("no.of object created", cls.count)
a = store("kurti",500)
b = store("shirt",300)
c = store("pants",800)
d = store("skirt",200)
e = store("apple",100)
f = store("phone",1000)
a.discount(10)
b.get_info()
store.get_count()