class emmployee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")

class developer:
    def __init__(self,program):
        self.program=program
    
    def show(self):
        print(f"the program is {self.program}")

class developeremployee(developer,emmployee): #this calls developer class show method
    def __init__(self, name,program):
        self.name=name
        self.program=program

class developeremployee(emmployee,developer): #this calls emmployee class show method
    def __init__(self, name,program):
        self.name=name
        self.program=program


e=developeremployee("raza","python")
print(e.name)
print(e.program)
print(e.show())
print(developeremployee.mro())