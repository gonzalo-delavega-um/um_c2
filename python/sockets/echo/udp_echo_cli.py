#!/usr/bin/python3
import socket

HOST = 'localhost'
PORT = 1234
MAX_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    data, address = s.recvfrom(MAX_SIZE)
    print('Connection established: %s:%i' % (address[0], address[1]))
    if data:
        s.sendto(data, address)

