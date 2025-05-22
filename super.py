# #super keyword is used to reffer the parent class

# class parentClass:
#     def parent_method(self):
#         print("parent method")

# class childclass(parentClass):
#     def parent_method(self):
#         print("raza")

#     def child_method(self):
#         print("this is child method")
#         super().parent_method() #calls parent class parent method and the output is parent method

# child=childclass()
# child.child_method()
# child.parent_method()  #calls childclass parent method and the output is raza

#another meethod for call consstructor of parent class
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id


class developer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

raza=Employee("raza",5)
ali=developer("ali",6,"python")
print(ali.name)
print(ali.id)
print(ali.lang)