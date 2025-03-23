# dictionary are orderd, stored multiple item in single variable. it has key value pairs

dec={
    "raza":"Human",
    "age":25,
}

# print(dec["raza"]) #output: Human

# print(dec.get("raza")) #output: Human i.e second way

# print(dec["raza1"]) #output: error

# print(dec.get("raza1")) #output none

# print(dec.keys()) #gives all keys

# print(dec.values()) #gives all values

# for key in dec.keys():
#     print(dec[key]) #gives all keys

# #OR by usinf f_string

# for key in dec.keys():
#     print(f"the value of {key} is {dec[key]}")

print(dec.items()) #gives key value pairs

for key,value in dec.items():
    print(f"the value of {key} is {value}") #gives key value pairs