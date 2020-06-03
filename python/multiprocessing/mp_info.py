from multiprocessing import Process
import os, time

def child1():
    print("Child 1",os.getpid())
#    print("hijo trabajando....")
#    time.sleep(4)

def child2():
    print("Child 2",os.getpid())


if __name__=="__main__":
   print("Parent ID",os.getpid())
   p1=Process(target=child1)
   p2=Process(target=child2)
   p1.start()
   p2.start()
   print("PID p1: %d" % p1.ident)
   print("PID p2: %d" % p2.ident)
#   os.kill(p1.ident, signal.asdfas)
   p1.join()
   alive='Yes' if p1.is_alive() else 'No'
   print("Is p1 alive?",alive)
   time.sleep(1)
   #os.system("ps fax")
   alive='Yes' if p2.is_alive() else 'No'
   print("Is p2 alive?",alive)
   p2.join()
   print("We're done")
