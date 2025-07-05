# Q. Write a class Student with marks of 3 subjects.Add method to Find total and average.
class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def total(self):
        return self.m1 + self.m2 + self.m3
    def average(self):
        return self.total() / 3

s= Student(80,90,85)
print("Total :",s.total())
print("Average :",s.average())