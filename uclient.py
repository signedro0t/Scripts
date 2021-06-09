#!/usr/local/bin/python3

import socket

target_host = "www.google.com"
target_port = 80

#SOCKET created
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#SEND data
client.sendto(b"AAAABBBBCCCC",(target_host,target_port))

#RECEIVE data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()