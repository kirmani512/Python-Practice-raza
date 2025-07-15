# Walrus operator is used to assign the value to variables within an expression. this can be useful when you have to use a value multiple times in a loop, but don't want to repeat the calculation

# a=True

# # print(a=False) this throws an error

# print(a:=False) #this is walrus operator

# numbers=[1,2,3,4,5]

# while(n:=len(numbers))>0:
#     print(numbers.pop())


#Example 2-------------------------------------------------------------------------------------------

# foods=list()

# while True:
#     food=input("enter the food")
#     if food=="quit":
#         break
#     foods.append(food)   this can be written as following

foods=list()

while(food:=input("Enter food : ")) !="quit":
    foods.append(food)
