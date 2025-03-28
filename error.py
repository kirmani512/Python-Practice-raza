a=input("Enter a number: ")

print(f"Table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i}={int(a)*i}")
# except Exception as e: #in case of error occured
#     print(f"An error occurred: {e}")
except:
    print("expected input is integer value")


print("end of program")

#we can use multiple excepts according to situation like
# except ValueError:
# except TypeError:
# except Exception as e: #for any other exception
#except indexerror