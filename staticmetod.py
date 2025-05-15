#static methods are used when you don't need the class instance
#it cann be called independentally

class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7,2))  #calling static method
print(a.add(7,3)) #another way to call method
