x= int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if(x!=80): 
        print(x,"Is not 80")
    case _ if(x!=70): 
        print(x, "is not 70")
    case _: #this shows defautl value means if no case match then this will match
        print(x)