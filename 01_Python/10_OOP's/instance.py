class laptop:
    storage = "ssd"
    @classmethod
    def storage_type(cls):
        print(f"laptop has {cls.storage}")
    @staticmethod
    def discount(price, discount):
        actual_price = price - (price*discount /100)
        print(f"the value of the laptop is {actual_price}")
    def __init__(self,ram,rom):
        self.ram = ram
        self.rom = rom
    def get_info(self):
        print(f"the laptop has {self.ram} , rom of {self.rom} and storage type {self.storage}.")
laptop1 = laptop("512 GB","16 GB")
laptop2 = laptop("256 GB","32 GB")
laptop1.get_info()
laptop2.storage_type()
laptop.storage_type()
laptop1.discount(50000,10)