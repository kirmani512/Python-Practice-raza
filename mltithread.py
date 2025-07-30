import threading
import time
from concurrent.futures import ThreadPoolExecutor

#indicates some task being done
def fn(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

#these functions execute one after other
# fn(4)
# fn(3)
# fn(2)

#for parallel call of functions 

def main():
    t1=threading.Thread(target=fn,args=[4])
    t2=threading.Thread(target=fn,args=[3])
    t3=threading.Thread(target=fn,args=[2])

#it takes time o seconds as it will not wait for t1 to end
    t1.start()
    t2.start()
    t3.start()

# t1.join() 
# t2.join() waits for t1 to end then it starts it total takes a time of 4s

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(fn,4)
        future2=executor.submit(fn,3)
        future3=executor.submit(fn,2)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()
