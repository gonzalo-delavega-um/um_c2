#import multiprocessing
from multiprocessing import Process
import os, time

def child1():
    print("Child 1",os.getpid())
    print("esperando..."); time.sleep(5)
    os.system("ps fax")
    print("hijo muriendo...")


if __name__=="__main__":
    print("Parent ID",os.getpid())
    p1=Process(target=child1)
#    p1.run()
    print("========================================================")
    print("Parent ID",os.getpid())
    p1.start()
    for i in range(10):
        print("Padre esperando a que el hijo muera...")
        time.sleep(1)
    print("PS FAX del padre (hijo muerto) -------------------------")
    os.system("ps fax")
    p1.join()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    os.system("ps fax")

    print("We're done")

    #p1.kill() # envia un SIG_KILL al p1
