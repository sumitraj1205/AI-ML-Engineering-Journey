class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("area = ",3.14 * self.radius *self.radius)
class rectangle(shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def area(self):
        print("area = ",self.length *self.breath)
class triangle(shape):
    def __init__(self,base,heigth):
        self.base = base
        self.heigth = heigth
    def area(self):
        print("area = ",1/2 * self.base *self.heigth)
a = circle(3)
b = rectangle(4,3)
c = triangle(8,3)
a.area()
b.area()
c.area()

