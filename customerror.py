user_input=input("Enter a number between 4 to 10")

if user_input.lower()=="quit":
    print("hi")

else:
    a-int(user_input)    

if(a<4 or a>10):
    raise ValueError("value should be between 4 to 10")
