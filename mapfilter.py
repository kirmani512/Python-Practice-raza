# #map function works like for loop means itterate on each object and returns a map object//////////////////////

# # def cube(x):
# #     return x*x*x

# # print(cube(2))

# l=[1,2,3,4,5,7]

# # newl=list (map(cube,l)) #it returns map object and can be converted into list like this

# newl=list (map(lambda x:x*x*x,l)) #can also be written as lamda instead of using cube function as an argument

# print(newl)

# #FILTER functions filters the data from the given list it also returns filter object and cann be coverted into list///////////////////

# def filer_function(a):
#     return a>5 

# filtered= list (filter(filer_function,l))
# print (filtered)

#REDUCE////////////////////////////////////////////////////////////////////////////////////

from functools import reduce

numbers=[1,2,3,4]

sum= reduce(lambda x,y:x+y,numbers) #it add first two numbers and make it x then add next number in that x like
#here after first iteration list will be [3,3,4],then [6,4] and at the end it is [10]

print(sum)