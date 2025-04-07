#Self practice-------------------------------------------------------

# l=["pakistan birthday","1947"]

# print(l[0])

# user_input=input()

# if user_input ==l[1]:
#     print("get 100")
# else:
#     print("you lose")

#final Solution------------------------------------------------------

questions=[
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
     ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
     ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],
    ["which language is used in fb","php","js","python",1],

       ]

level=[1000,2000,3000]
amount=0
for i in range(0,len(questions)):
    question= questions[i]
    print(f"question for rs {level[i]}")
    print(f"a. {question[i][1]}                  b. {question[i][2]}                  c. {question[i][3]}")
    reply=int(input("enter your answer between 1 to 3"  ))
    if reply==question[-1]:
        print(f"you win rs {level[i]}")
        if(i==3):
            money=10000
        elif(i==9):
          money=5000
    else:
        print("you lose")
        break