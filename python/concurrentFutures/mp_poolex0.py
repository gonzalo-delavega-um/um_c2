from concurrent.futures import ProcessPoolExecutor
from time import sleep
import os

def return_after_5_secs(message):
    sleep(5)
    print("Saliendo %d" % os.getpid())
    return message

pool = ProcessPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
sleep(6)
print(future.done())
print(future.result())
