
class student:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"the name is {self.name} str"
    
    def __repr__(self):
        return f"student('the name is '{self.name}'). repr" 
    
    #repr return what you need to see about your class in debugging messags

    #str to retrun what is useful when asked to show to humans

    def __call__(self):
        print("Hi by call method")