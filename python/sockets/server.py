#!/usr/bin/python3
import socket, sys

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
"""
    socket.AF_INET -> sockets tcp/ip
    socket.AF_UNIX -> sockets Unix (archivos en disco, similar a FIFO/named pipes)

    socket.SOCK_STREAM -> socket tcp, orientado a la conexion (flujo de datos)
    socket.SOCK_DGRAM -> socket udp, datagrama de usuario (no orientado a la conexion)
"""

# get local machine name
host = socket.gethostname()                           
#host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    msg = 'Hola Mundo'+ "\r\n"
    #clientsocket.send(msg.encode('ascii'))
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
