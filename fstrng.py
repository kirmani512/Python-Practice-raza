letter= "i am {1} lives in {0}"

name="raza"

city="lahore"

print(letter.format(city,name))   #this is previous approach

print(f"i am {name} lives in {city}") #this is f-string that allows to use variable inside string

print(f"i am {{name}} lives in {{city}}") #it shows as it is instead of populating values  from variables

txt="price is {price:.2f}"  #gives two decimal values

print(txt.format(price=80.09420))

print(f"{2*2}")