class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show(self):
        print(f"the name of the employee {self.id} is {self.name} ")

#inheritance/////////////////////////////////////
class developer:
    def stack(self):
        print("The stack is mern")

e=employee("raza",5)
e.show()
e1=employee("hassan",7)
e1.show()

e2=developer()
e2.stack()