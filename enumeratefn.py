
marks=[12,13,45,65,66,543,456]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("welldone")
#     index+=1

#short method to do the  above code  by enumerate function

for index,mark in enumerate(marks,start=1): #index can be channged with atart
    print(mark)
    if(index==3):
        print("welldone")
