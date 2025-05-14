#snake water gun 

import random #yoou cann generate random intgers with this module

def check(system,user):

    if system==user:
        return 0   #score level
    
    if(system==0 and user==1):
        return -1 #you lose
    
    if (system==1 and user==2):
        return -1
    
    if (system==2 and user==0):
        return -1
    
    return 1 #win

system=random.randint(0,2) #choose number b/w 0 to 2

user=int(input("o for snake, 1 for water, 2 for gun,\n"))

score=check(system,user)

print("you", user)

print("system",system)

if(score==0):
    print("draw")

elif (score==1):
    print("you win")

else:
    print("you lose")