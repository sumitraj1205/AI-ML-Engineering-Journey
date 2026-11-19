class constructor:
    def __init__(self,name,age =None,address = None):
        self.name = name
        self.age = age
        self.adress = address
    def display(self):
        print('name-',self.name)
        if self.age!=None:
            print("age is-",self.age)
        if self.adress!=None:
            print("address is-",self.adress)   
user1 = constructor("sumit")
user2 = constructor("kunal",22)
user3 = constructor("ravi",20,"nalanda")
user1.display()
user2.display()
user3.display()