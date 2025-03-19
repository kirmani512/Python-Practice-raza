#tuples are datatypes and similar to list the only difference is tuples can't be changed
tup=(1, "red",4,5,7)
print(type(tup),tup)
print(tup[1])
print(tup[-1])

if "red" in tup:
    print("yes it is in tup")

#slicing can be done by returning new tuple
tup2=tup[1:4] #returns from index 1 to 4 fourth index is not  included but 1 index is included
print(tup2)


#tuple cana be conerted into list then make changes in that list then again change into tuple