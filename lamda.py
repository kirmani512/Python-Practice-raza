#lambda  function is a small anonymous function which can take any number of arguments but have only one expression
#mostly it is  used when you pass the fn as an argument

sum= lambda x:x+5

cube=lambda x:x*x*x   #insted of writing whole function lamda helps to short the function

avg=lambda x,y:(x+y)/2  #can take muttiple arguments

avg2=lambda x,y,z:(x+y+z)/3  #can take muttiple arguments


print(sum(5))

print(cube(2))

print(avg(5,3))

print(avg2(5,3,10))