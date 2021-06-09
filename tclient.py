#!/usr/local/bin/python3

import socket

target_host = "www.google.com"
target_port = 80

#SOCKET Create
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONNECT to client
client.connect((target_host, target_port))

#SEND data
client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#RECIEVE data
response = client.recv(4096)

print(response.decode())