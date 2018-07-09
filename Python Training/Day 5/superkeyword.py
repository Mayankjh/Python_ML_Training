class Person:
    def __init__(self,first,last):
        self.firstname =first
        self.lastname = last
    def __str__(self):
        return self.firstname + " " + self.lastname
class Employee(Person):
    def __init__(self,first,last,staffnum):
        super().__init__(first,last)
        self.staffnumber = staffnum
x = Person("Dhila", "simpson")
y = Employee("BABA","khatri",420)
print(x,y)