from multiprocessing import Process, Value, Array, Pool
import os
import signal
import time


num=0

def sumador():
    global num
    print(num)
    num+=1


num = 1
for i in range(10):
    p = Process(target=sumador)
    p.start()

time.sleep(1)

print(num)
