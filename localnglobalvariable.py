x=10

def myfn():
    global x  #to change the value of global variable 
    x=4
    y=5

    print(y)

myfn()
print(x)
print(y)