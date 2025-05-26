#method overriding is when a parent fn is changed in child class according to requirements

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):                                                     #method overriding
        return 3.14 * super().area()
    
rec=shape(2,5)

print(rec.area())

c=circle(5)  

print(c.area())