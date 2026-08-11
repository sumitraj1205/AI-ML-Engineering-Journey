from abc import ABC, abstractmethod
class animal:
    @abstractmethod
    def make_sound(self):
        pass
class dog:
    def make_sound(self):
        print("bark")
class lion:
    def make_sound(self):
        print("roar")
class cat:
    def make_sound(self):
        print("meow")
a = lion()
a.make_sound()
        
        