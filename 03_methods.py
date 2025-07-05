# Method mean Function inside class.
class Student:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"Hello, my name is { self.name}")

s1=Student("Rahul")
s1.greet()  #output: Hello, my name is Rahul