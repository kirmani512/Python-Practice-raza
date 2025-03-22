# s={1,2,5,6}

# s1={3,4,6,7}

# # print(s.union(s1))

# # print(s.update(s1)) #updates the s set with s1 values whic are not in s

# # print(s,s1)

# #intersection-------------------------------------------------------------------------

# # print(s.intersection(s1))

# # s.intersection_update(s1)

# # print(s)

# #symetric difference means gives that vlaues which are not common in both sets

# s2=s.symmetric_difference(s1)

# print(s2)

#difference------------------------------------

#it removes the value from ist set i.e num that are common in num 2 i.e a-b

# num={1,2,3,4,5,6,7}

# num2={0,9,8,1,2}

# num3=num.difference(num2)

# num.difference_update(num2)

# print(num3)

# print(num)

#disjoint sets i.e if two sets have no element in common it returns true or false---------

# val={1,2,3,4,5}

# val2={5,6,7,7}

# print(val.isdisjoint(val2))

#is superset method check if second set elemnts are in first set or not-------------

# val={1,2,3,4,5}

# val2={5}

# print(val.issuperset(val2))

#issubset checks the second set is the subset of first or not means check the values present in first-------

# val={1,2,3,4,5}

# val2={5}

# print(val2.issubset(val))

#add method adds a single item in set

# val={1,2,3,4,5}

# val.add(6)

# print(val)

#update method is used if you want to add more than one items---------------------------

# val={1,2,3,4,5}

# val2={6,7}

# val.update(val2)

# print(val)

#remove is used to remove the item from the set--------------------

# val={1,2,3,4,5}


# val.remove(1)

# print(val)

#difference between remove and discard is remove arise the error if the item is not present in the set while discard does not

# val={1,2,3,4,5}


# val.discard(6)

# print(val)

#pop method picks the random value from the set-------------

# val={1,2,3,4,5}


# val2=val.pop()

# print(val2)

#del method deletes the whole set and araise an error----------------

# val={1,2,3,4,5}


# del val

# print(val)

#clear is used to delete the entreis from set not the set

# val={1,2,3,4,5}


# val.clear()

# print(val)

#in tells weather the item is in set or not

val={1,2,3,4,5}

if 7 in val:
    print("yes it is")
else:
    print("no it is not")