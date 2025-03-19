import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
# timestamp=time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
hour=int(time.strftime('%H'))
if(hour<9):
    print("Have a good day")
else:
    print("Good Night")