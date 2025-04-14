import pandas
import math
from math import sqrt,pi     #to import some specific functions instead  of all library
from math import sqrt as s   #can also be imported as this for short hand

from raza import welcome,raza  #imported from raza.py

#or-------------

from raza import *

# pandas.read_csv
# math.floor(2.23)

# result=math.sqrt(9) #for import math

# result1=sqrt(9)*pi  #for from

# result2=s(16)

# print (result)

# print(result1)

# print(result2)

print(dir(math)) #the dir fn is used to print all the functions in module

print(math.nan,type(math.nan))
welcome()
print(raza)