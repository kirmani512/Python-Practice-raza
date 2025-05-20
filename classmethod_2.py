#class method as alternative constructors

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])  #class method as alternative constructor
e=Employee("raza",25000)
print(e.name)
print(e.salary)

string="ali-4000"
# e2=Employee(string.split("-")[0],string.split("-")[1])  By adding this in fn now we cann access the e2 
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)