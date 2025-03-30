#the code written in finally always execute weather it is error or not or function returns a value as after return of fn it skips remaining code but with finally fn is not able to skip

# try:
#     l=[1,2,3,4,5]

#     i=int(input("Enter a number"))

#     print(l[i])

# except:
#     print("error")

# finally:
#     print("Always execute")


#OR----------------------------------------------

def fn():
    try:
        l=[1,2,3,4,5]

        i=int(input("Enter a number"))

        print(l[i])

        return 1

    except:
        print("error")

        return 0

    finally:
         print("Always execute")

x=fn()

print(x)