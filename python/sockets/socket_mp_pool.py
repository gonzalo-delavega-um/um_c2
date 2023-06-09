#!/usr/bin/python

"""
    Pool of Workers
"""


from multiprocessing import Pool, TimeoutError
import time
import os
import random
import socket
import sys



def mp_server(c):
    print("Launching proc...")
    sock,addr = c
    while True:
        msg = sock.recv(1024)
        print("Recibido: '%s' de %s" % (msg.decode(), addr))
        msg = "Ok"+" \r\n"
        sock.send(msg.encode("ascii"))
        #clientsocket.close()


pool = Pool(processes=4)

# create a socket object
# crea un objeto tipo socket para usarlo en la comunicación
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
#host = socket.gethostname()
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    cliente = serversocket.accept()

    clientsocket, addr = cliente

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    res = pool.apply_async(mp_server, args=(cliente,)) # runs in *only* one process
