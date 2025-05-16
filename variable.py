#instance vs class varibales

#we use instance varibales when we have to associate any property with a particular object

#class varibales are used when we have to create a variable for whole class

class Employee():
    company="Hyetelx" #class variable i.e associated with class
    def __init__(self,name):
        self.name=name
        self.raiseamount=10 #instance variable
    def showdetails(self):
            print(f"the name of the employee is {self.name} and the increment in the company {self.company} is {self.raiseamount}")

emp1=Employee("raza") #instance variable

emp1.raiseamount=20 #it can be changed here 

emp1.company="orbin" #if instance varible is present then it can be changed otherwise it calls class variable

emp1.showdetails()

# Employee.showdetails(emp1) #another way for this emp1.showdetails()
emp2=Employee("hassan")
emp2.showdetails()


