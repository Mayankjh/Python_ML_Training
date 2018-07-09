#

class Emp:
    empCount = 0
    def __init__(self,name, salary):
        self.name =  name
        self.salary = salary
        emp.empCount += 1
    def displayCount(self):
        print("total emp %d",emp.empCount)
    def dispEmployee(self):
        print("Name:", self.name, "Salary: ",self.salary)
emp1 = Emp("sara",2000)
emp1.displayEmployee()
print("total employee %d")
    