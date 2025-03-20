#set is a collection of unordered well defined objects it is used to avoid duplication of values in python
# they are unchangeable
# due to unordered behaviour they can't be accessed using index numbers

s={1,2,3,3,2,1}

print(s)

raza={}

print(type(raza)) #this is dect type

# for making empty set

raza1=set()

print(type(raza1))

# for accessing values in set

for value in s:
    print(value)