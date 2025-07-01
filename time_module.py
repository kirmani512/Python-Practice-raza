#time.time() returns a float value which represents the time in seconds since the epoch

import time

# def usingwhile():
#     i=0
#     while i<5000:
#         i=i+1
#         print(i)

# def usingfor():
#     for i in range(5000):
#         print(i)

# init=time.time()
# usingfor()
# t1=time.time()-init #returns the second which are paseed till this step

# init=time.time()
# usingwhile()
# print(time.time()-init) 
# print(t1)

#time.sleep()-------------------------------------------------------------------------------------------------
# print(4)
# time.sleep(3)  #gives a delay for 3 seconds
# print("Printed after 3 seconds")

#strftime----------------------------------------------------------------------------------------------
#gives time in required format
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)

print(formatted_time)