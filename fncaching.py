# Function caching is used when a function runs multiple times for the same value

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(10))
print("done for 10")
#In above print commands it takes 5 seconds to run but in below commands it runs on the same time due to lru_cache 
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(10))
print("done for 10")