class marks():
    def __init__(self,value):
        self.value=value

    def show(self):
        print(f"value is {self.value}")

#getters are used to access the value of an object
    @property  #property decorator makes it getter
    def double_value(self):
        return 2*self.value
    
    #setter////////////////////////////////////////////////////////////////////////
    @double_value.setter  
    def double_value(self,new_value):
        self.value=new_value*10
        
obj=marks(20)
print(obj.double_value)
obj.double_value=3
obj.show()