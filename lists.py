# #list can be changed but tuple can't be changed
# marks=[3,5,6,"raza",True,10,12,13,34,45,34,56] #can also add strings and bollean in lists
# # print(marks)
# # print(marks[0])

# # print(marks[-3]) #negative indexing it works in this way that it counts the length and then -3 indexes from the end here it shows 6
# # print(marks[len(marks)-3]) #positive indexing conversion
# # print(marks[5-3]) #this is how it works
# # print(marks[2])

# # if 7 in marks:   #to check the entry is in list or not
# #     print("yes")
# # else:
# #     print("no")

# # #same thing is applied for string as well

# # if "az" in "raza":
# #     print("yes")

# # print(marks[:]) #it also print all string
# # print(marks[1:]) #it starts from index 1
# # print(marks[1:-1])
# # print(marks[1:len(marks)-1])
# print(marks[1:8]) #it picks from index 1 to 3
# print(marks[1:8:2]) #jump index i.e jumps 2 index

#list comrehnesion ---------------------------------------------
# lst=[i for i in range(4)]
lst=[i*i for i in range(4)]

print(lst)
lst=[i*i for i in range(4) if i%2==0]

print(lst)