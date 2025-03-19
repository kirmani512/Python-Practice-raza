# # # # # # import pandas
# # # # # # import hashlib

# # # # # # #dont remove this

# # # # # # '''
# # # # # # this
# # # # # # is
# # # # # # multiline comment

# # # # # # '''
# # # # # # print("Hello \"World\"\n new to python")

# # # # # # print("Seprator",6,7,8,sep="~",end="00\n")

# # # # # # print("Raza")

# # # # # # a=10

# # # # # # a1=8
# # # # # # print(a)

# # # # # # b="ali"

# # # # # # print(b)

# # # # # # print(a+a1)

# # # # # # print("the type is", type(b))

# # # # # # # Everything in python is Object

# # # # # # print(15/6)
# # # # # # print(15//6) #Float division operator

# # # # # # print(15%6)  #modulus operator i.e. it gives remainder

# # # # # # print(5**2) #exponential operator


# # # # # # #calculator-----------------

# # # # # # print(a+a1)
# # # # # # print(a-a1)
# # # # # # print(a*a1)
# # # # # # print(a/a1)


# # # # # #Typecasting------------------------------
# # # # # # The conversion of one data type to annothe is typecastig

# # # # #two types
# # # # # 1. Implicit typecasting .i.e done by python
# # # # # 2. Explicit typecasting .i.e done by myself

# # # # a="10"
# # # # b="2"

# # # # print(a+b)  #output will be 102 bcz it takes it as a string

# # # # #explicit typecasting

# # # # print(int(a)+int(b))  #output 12

# # # # a=input("Enter your Name: ")

# # # # print("hi",a)

# # # # x=input("Enter first number: ")
# # # # y=input("Enter second number: ")

# # # # print(x+y) #output will be concatenation of two strings

# # # # print(int(x)+int(y)) #output will be addition of two numbers

# # # #strings---------------------------

# # # name="Raza"
# # # apple='''Hi said 
# # # "I like apple"
# # # I am good'''


# # # # print("Hi", name)
# # # # print(apple)

# # # print(name[0])
# # # # print(name[4]) #throws an error

# # # #for loop with strings

# # # for character in apple:
# # #     print(character) #prints each character of the string

# # #string slicing---------------

# # names="raza,ali"
# # nm="harry"
# # print(len(names))
# # print(names[0:3]) #prints raz i.e. includes zero but not 3
# # print(names[4:7]) #prints ,al
# # print(names[0:-3]) #prints raza,
# # print(names[0:len(names)-3]) #prints raza,
# # print(names[-1:len(names)-3])
# # print(names[-3:-1]) #prints al because it starts from -3 and ends at -1 and done by minus from length
# # print(len(nm))
# # print(nm[-4:-2]) #prints ar


# #String Methods--------------------------------------------------------------------
# #strings are immutable .i.e. can never be changed

# a="@raza !!!!!!!!!!! mehmood"
# print(a.upper()) #and the same for lower and it will not change the  existing string but returns the new strin
# print(a.rstrip("!")) #it strips the sign it only reoving the trailing sign not the starting signn
# print(a.replace("@raza","mehmood"))
# print(a.split(" ")) #it splits the string into list of strings

# heading="intro " " to python to"
# heading1="123"

# print(heading.capitalize()) #it makes the I of intro in capital
# print(heading.center(50)) #add 50 Spaces to the string and center it
# print(heading.count("t")) #it counts the number of t in the string
# print(heading.endswith("n")) #it checks if the string ends with n and returns true
# print(heading.endswith("to",2,8)) #it slices the string and checks wheather it ends with to at index 8
# print(heading.find("to")) #returns first occurance index and if not found it returns -1
# # print(heading.index("too")) #works same as find only the difference is it gives an error instead of -1 if not found
# print(heading1.isalnum()) #returns true if stirng is alpha numeric    An "alphanumeric" string is a string that contains both letters and numbers, and sometimes also includes special characters. ABC123 is an example of an alphanumeric string.
# print(heading.isalpha()) #alpha does not have numbers
# print(heading.islower()) #returns true if all characters are in lower case
# print(heading.isprintable()) #returns true if all characters are printable and false if string has \n or this type of characters
# print(heading.isspace()) #returns true if there is space
# print(heading.istitle()) #returns true only if the first letter of the string is capital
# print(heading.isupper())
# print(heading.startswith("i"))
# print(heading.swapcase()) #converts lower to upper case and vice versa
# print(heading.title()) #converts all the string first letters capital


#IF Else-----------------------------------------------------------------------------

a=int(input("Enter your age"))
print("your age is:", a)

if(a>18):
    print("You can drive")
else:
    print("you can't") #the space before print is indentation in python

#another example

appleprice=210
budget=200
if(appleprice<=budget):
    print("you can buy")
elif(appleprice-budget==10):
    print("you can buy")
else:
    print("you can't")

#Nested If------------
num=30
if(num<0):
    print("Num is negative")
elif(num>0):
    if(num>20):
        print("Num is greater than 20")
    elif(num>20 and num<=30):
        print("num is equal or between 0-30")
    else:
        print("num is not recognized")
else:
    print("num is zero")
