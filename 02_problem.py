#Q.Create a class circle with radius as an attribute.Add a method to calculate area and perimeter.
import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2 * math.pi *self.radius

c= Circle(5)
print("Area:",c.area())
print("perimeter : ",c.perimeter())