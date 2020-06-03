

from multiprocessing import Process

def testing():
    print("Works")

def square(n):
    print("The number squares to ",n**2)

def cube(n):
    print("The number cubes to ",n**3)

def multip(n,m):
    print("The product is: ", n*m)

if __name__=="__main__":
    p1=Process(target=square,args=(7,))
    p2=Process(target=cube,args=(3,))
    p3=Process(target=testing)
    p4=Process(target=multip,args=(4,5))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("We're done")
