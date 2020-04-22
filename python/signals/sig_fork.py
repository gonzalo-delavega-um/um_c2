#!/usr/bin/python3
import os,time,signal

def handler(s,f):
    print("mensaje... PID: %d" % (os.getpid()))

def hijo():
    print("Iniciando hijo PID: %d" % os.getpid())
    while True:
        print("Hijo esperando...")
        signal.pause()


def main():
    signal.signal(signal.SIGUSR1,handler)
    pid=os.fork()

    if pid == 0:
        hijo()
    else:
        print("Iniciando padre PID: %d" % os.getpid())
        for item in range(10):
            time.sleep(5)
            os.kill(pid,signal.SIGUSR1)
        print("Padre matando al hijo...")
        os.kill(pid,signal.SIGTERM)
        print("Padre terminando...")


if __name__ == "__main__":
    main()
