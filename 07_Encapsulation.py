# Encapsulation (Hiding data)
class Student:
    def __init__(self):
        self.__marks = 0  # Private variable

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(95)
print(s.get_marks())  # 95
