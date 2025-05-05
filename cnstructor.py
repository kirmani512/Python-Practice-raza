class person():
    def __init__(self,n,a):  #it invokes on each call
        print("I am a constructor")
        self.name=n
        self.age=a

    def info(self):
        print(f"{self.name} age is {self.age}")


a=person("raza",28)
b=person("hassan",30)

a.info()
b.info()