#classes are used to make custom data types
class Employee:
    company="hyetel"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

    @classmethod #this will change the company name in class if i use this decorator it takes first argument as class instead of instance by default it takes  first argument as instanace
    def changename(self,newcompany):
        self.company=newcompany


    
e1=Employee()
e1.name="raza"
e1.show()
e1.changename("orbin")
e1.show()
print(Employee.company) #this will show hyetel