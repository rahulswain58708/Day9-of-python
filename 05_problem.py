#Q.Create an Employee class and subclass Manager. Add extra attribute bonus in Manager.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus

m = Manager("Rahul",30000,500)
print(f"Total Salary : Rs.{m.total_salary()}")