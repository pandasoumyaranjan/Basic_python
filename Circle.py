import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

r = int(input("Enter radius of the Circle : "))
obj = Circle(r)
print("Area of the Circle is : ",obj.area())
print("Perimeter of the Circle is :",obj.perimeter())
print()