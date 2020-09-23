import os
import multiprocessing, threading, time, getopt, sys

def func(x):
    while True:
        dato = x.recv()
        if dato==404:
            print("Proc %s saliendo..." % multiprocessing.current_process().name)
            break
        print("Funcion, recibido %s" % str(dato))
        x.send("ok  %d (%s)" % (dato,multiprocessing.current_process().name))


def server(x, n):
    print("Server %s recibiendo lista %s" % (threading.current_thread().getName(), str(n)))
    for i in n:
        x.send(i)
        print("Server %s recibiendo: %s" % (threading.current_thread().getName() ,x.recv()))
        time.sleep(1)
    x.send(404)


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def usage(progname):
    print("\n\tpython3 %s -p <num_proc> -n <num_max>\n\n" % progname)
    sys.exit(2)




if __name__ == "__main__":

    n = 0
    nproc = 0

    print(len(sys.argv))
    if len(sys.argv) != 5:
        usage(sys.argv[0])

    (opt,arg) = getopt.getopt(sys.argv[1:], 'p:n:', ["nproc=", "max="])

    for (op,ar) in opt:
        if(op in ['-p', '--nproc']):
            nproc = int(ar)
        elif(op in ['-n', '--max']):
            n = int(ar)
        else:
            usage(sys.argv[0])


    x = list(range(n))
    partes = split_list(x, nproc)

    for part in partes:
        a,b = multiprocessing.Pipe()
        p = multiprocessing.Process(target=func, args=(a,))
        h = threading.Thread(target=server, args=(b,part))
        p.start()
        h.start()
