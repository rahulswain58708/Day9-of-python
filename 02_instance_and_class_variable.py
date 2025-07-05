class Student:
    school="ABC School" # Class Variable 

    def __init__(self,name):
        self.name=name  # instance Variable


s1=Student("Rahul")
s2=Student("Aman")

print(s1.name) # Rahul
print(s2.name)# Aman
print(s1.school)# ABc School
print(s2.school)# ABC School