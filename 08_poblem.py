# Q. Create a class Shape with abstract method area(). implement Rectangle and circle using inheritance.\
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):

        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    
    def area(self):
        return self.l * self.b
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi * self.r **2

r= Rectangle(5,4)
c= Circle(3)
print("Rectangle Area : ",r.area())
print("Circle Area:",c.area())