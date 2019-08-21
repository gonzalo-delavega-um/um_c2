
from multiprocessing import Pool
import os
import signal
import time

def sumador(x):
    x = x+1

def pid(x):
    return ("pid: %d - x=%d" % (os.getpid(), x))

def cube(x):
    print("Proceso %d calculando cubo de %d" %(os.getpid(), x))
    return x**3

pool = Pool(processes=4)

input("Pool.map")
results = pool.map(cube, range(15))


input("Pool.apply")
results = [pool.apply(cube, args=(x,)) for x in range(15)]
print(results)

input("Pool.apply again...")
results=[]
for x in range(15):
    results.append(pool.apply(cube,args=(x,)))
print(results)


input("Pool.map_assync")
results=[]
results.append(pool.map_async(cube, range(15)))
#results.get()
print("espereando...")
time.sleep(1)
print(results[:-1])


input("Pool.apply async...")
results=[]
for x in range(15):
    results.append(pool.apply_async(cube,args=(x,)).get())

print("espereando...")
time.sleep(1)
print(results)

