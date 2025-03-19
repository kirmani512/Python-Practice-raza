# #four types of arguments
# def average(a=4,b=6): #these are default arguments
#     print("the average is" , (a+b)/2)
# average(1,1) #now it picks these arguments instead of the default ones
# average(1) #you can give one argment here too this assumes as a value
# average(b=10) #this assumes b


#keyword arguments------------------------------------------------------------------------
# average(b=10,a=20) #this is keyword argument

#reuired argument means the value must be given

#variable length argument----------------------------
def average(*numbers): #this take nmbers as a tuple
    sum = 0
    for i in numbers:
        sum=sum+i
    # print("averagae is" , sum/len(numbers)) #thiis can also be done by return like
    return sum/len(numbers)
        
# average(5,5,2)
c=average(5,5,2)
print(c) #this will print the average of the numbers passed to the function