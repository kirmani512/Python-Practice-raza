# generators are special type of iterable and are difeerent from list bcz in list value is already there but generator generate on the fly values
# it doesn't store the value but store the info by whom value can be build up

def my_generator():
    for i in range(50):
        yield i #yield returns a value from generator and suspend the execution

gen=my_generator()
# print(next(gen)) #output will be 0 
# print(next(gen)) #output will be 1
# print(next(gen)) #output will be 2 
# print(next(gen)) #output will be 3 


#another way to use generator///////////////////////////
for g in gen:
    print(g)