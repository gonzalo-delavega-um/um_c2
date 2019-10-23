
<<<<<<< HEAD
=======
from multiprocessing import Process, Lock
>>>>>>> 3ead036746115a6d35af794fa5e58b401cea114e
import threading
import time

def f(l, n):
    l.acquire()
    for i in range(3):
        print ("hello world %d %d" % (n,i))
        time.sleep(1)
    l.release()

<<<<<<< HEAD

def f_with(l,n):
    """Ejemplo con with, se llama al acquire cuando se entra al bloque, y al release cuando se sale"""
    with l:
        for i in range(3):
            print ("hello world %d %d" % (n,i))
            time.sleep(1)

=======
>>>>>>> 3ead036746115a6d35af794fa5e58b401cea114e
if __name__ == '__main__':
    lock = threading.Lock()

    for num in range(2):
        threading.Thread(target=f, args=(lock, num)).start()
<<<<<<< HEAD

    for num in range(2):
        threading.Thread(target=f_with, args=(lock, num)).start()
=======
>>>>>>> 3ead036746115a6d35af794fa5e58b401cea114e
