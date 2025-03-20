#caliing the same function inside a function is recursion

#factorial(5)= 5*4*3*2*1

#factorial(0)= 1 by defination

#similarly 

#factorial(n)= n*factorial(n-1)

#e.g factorial(5)= 5*factorial(5-1 i.e 4)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) #this is recursion i.e fn calling itself

print (factorial(3))