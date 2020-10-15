#!/usr/bin/python
import threading, time

balance = 0 

def deposit(amount):
    print ("deposito")
    global balance
    balance = balance + amount
    print("balance: %d" % balance)

def extract(amount):
    time.sleep(5)
    global balance
    print ("extraccion")
    balance = balance - amount
    print("balance: %d" % balance)


if __name__ == "__main__":
    th = []
    th.append(threading.Thread(target=deposit, args=(30000,)))
    th[-1].start()
    th.append(threading.Thread(target=extract, args=(8000,)))
    th[-1].start()
    
    for i in th:
        i.join()

    print("Final balance: %d" % balance)
