#!/usr/bin/python3
import socket, os, multiprocessing

def mp_server(sock):
    print("Launching thread...")
    while True:
        msg = sock.recv(1024)
        print("Recibido: %s" % msg.decode())
        msg = "Ok"+" \r\n"
        sock.send(msg.encode("ascii"))
        #clientsocket.close()



# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()
host = ""
port = 1234

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    child = multiprocessing.Process(target=mp_server, args=(clientsocket,))
    child.start()

