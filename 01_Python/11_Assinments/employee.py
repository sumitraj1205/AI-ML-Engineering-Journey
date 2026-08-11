from abc import ABC , abstractmethod
class employe(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class intern(employe):
    def __init__(self,days,salary):
        self.days = days
        self.salary = salary
    def calculate_salary(self):
        print("salary = ", self.days*self.salary)
class full_time_employe(employe):
    def __init__(self,salary):
        self.salary = salary
    def calculate_salary(self):
        print("salary = ", self.salary)
class contract_employe(employe):
    def __init__(self,days,salary):
        self.days = days
        self.salary = salary
    def calculate_salary(self):
        print("salary = ", self.days*self.salary)
sumit = intern(60,100)
kunal = full_time_employe(50000)
ravi = contract_employe(65,200)
sumit.calculate_salary()
kunal.calculate_salary()
ravi.calculate_salary()