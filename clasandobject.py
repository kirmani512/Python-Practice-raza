class person:
    name="raza"
    age=28
    def info(self): #self is the refernce to the current instance or object of the class like if we call a.info it calls a and if we call b.info it gets b variable values
        print(f"{self.name} age is {self.age}")

a=person() #object

b=person()

a.name="hassan"
a.age=30

b.name="ali"
b.age=35
# print(a.name,a.age)

a.info()
b.info()