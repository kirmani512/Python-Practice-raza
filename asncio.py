import time
import asyncio

async def fun1():
    await asyncio.sleep(1)
    print("fn 1")
    return "raza"

async def fun2():
    await asyncio.sleep(1)
    print("fn 2")

async def fun3():
    await asyncio.sleep(4)
    print("fn 3")

async def main():
#   task=asyncio.create_task(fun1()) to schedule tasks/////////
#   await  fun1()
#   await fun2()
#   await fun3()
# for parallel run of all functions use asyncio.gather////////////
    l=await asyncio.gather(
    fun1(),
    fun2(),
    fun3(),
    )
    print(l)

asyncio.run(main())