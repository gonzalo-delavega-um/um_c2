import threading, signal, os

def handler(s,f):
    print("Señal: ", threading.current_thread().name)

def f1():
    signal.signal(signal.SIGUSR1, handler)
    signal.pause()
    print("fin hilo")

if __name__ == "__main__":
    print(os.getpid())
    t1 = threading.Thread(target=f1)

    t1.start()
    signal.pause()
    print("Fin main")
