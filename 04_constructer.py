class Student:
    def __init__(self,name="unknow"):
        self.name=name

s1=Student()
s2=Student("Rahul")
print(s1.name) #unknow
print(s2.name) #Rahul