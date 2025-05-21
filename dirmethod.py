#object introspection means what is present in an object
#there are three built in functions
#dir
#__dict_
#help

#dir//////////////////////////////////////////////////////////////////
# x=[1,2,3] #it can also be tople i.e y

# y=(4,5,6)

# print(dir(x)) #check the methods in the list
# print(x.__add__)

# print(dir(y)) #check the methods in the tople
# print(y.__add__)

#__dict__///////////////////////////////////////////////////////////////

class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age   

p=person("raza",30)
print(p.__dict__) #gives all the class attributes like self.name and self.age as a dictionary


#help//////////////////////////////////////////////////////////////////////
#it is used to get help documentation of ann object

print(help(person))