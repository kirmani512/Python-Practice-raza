#operator overloading is a method by which you can change the behavior of operators

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):  #operator overloading
        # return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k"
        return vector(self.i+x.i , self.j+x.j , self.k+x.k)


v=vector(2,3,4)

print(v)

v1=vector(5,6,7)
print(v1)

print(v+v1)

print(type(v+v1))