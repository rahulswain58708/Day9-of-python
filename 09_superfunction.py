class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

s= Student("Rahul",101)
print(s.name) #Rahul
print(s.roll) #101