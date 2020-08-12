

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

    p = []
    p[0]=Process(target=square,args=(7,))
    p[1]=Process(target=cube,args=(3,))
    p[2]=Process(target=testing)
    p[3]=Process(target=multip,args=(4,5))

    for i in range(4):
        p[i].start()

    for i in range(4):
        p[i].join()

    print("We're done")
