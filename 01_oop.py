class Student: # create class
    def __init__(self,name,age):
        self.name=name # instance Atribute
        self.age=age
# create object
s1=Student("Rahul",18)
print(s1.name)
print(s1.age)