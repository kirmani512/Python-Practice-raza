# #decorators change the function like it simply gets a function as an argument and returns functioon after changing
# def greet(fx):
#     def mfx():   #mfx i.e modified fn
#         print("Good Morning")
#         fx()
#         print("Decorators")
#     return mfx

# @greet  #tells to decorate hello fn it can also be writeen as greet(hello())
# def hello():
#     print("Hello world")

# hello()
#another case/////////////////////////////////////////////////////////

def greet(fx):
    def mfx(*args,**kwargs):   #*args takes all arguments as tople and **kwargs take key value pair as dicitionary
        print("Good Morning")
        fx(*args,**kwargs) #it will works without **kwargs
        print("Decorators")
    return mfx

@greet
def add(a,b):
   print(a+b)

add(1,1)