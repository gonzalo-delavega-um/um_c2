from multiprocessing import Process, Lock
import time

lock=Lock()

def printer(item):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

def concurrent1():
    items=['hola','mundo',123123, 1111111,'que tal']
    for item in items:
        p=Process(target=printer,args=(item,))
        p.start()


if __name__=="__main__":
    concurrent1()
