#Q.create a class person with attribute name and age .write a method display the person's info.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name : {self.name},age:{self.age}")
p= Person("Rahul",18)
p.display()