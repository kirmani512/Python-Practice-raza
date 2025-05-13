#access modifiers/////

#all variables are by default public in python//////////

#public////////////////////

# class student:
#     def __init__(self):
#         self.name="Raza"

# a=student()
# print(a.name)

#private----------->In prvate if you add double underscore as prefix with varubale it will be considered as private

class student:
    def __init__(self):
        self.__name="Raza"

a=student()
print(a._student__name) #it can be accessed like this this is called name mangling in python
#name mangling is a technique used in Python to protect variables from being accidentally overwritten

#protected variables are accessed within the class and the classes derived from that class


