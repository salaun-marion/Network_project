#NOT WORKING AT ALL ^^

import socket

client_sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = "This is UDP client : File downloaded"

client_sock.sendto(message.encode('utf-8'),('127.0.0.1',12345))

data, addr=client_sock.recvfrom(4096)
print(str(data))
client_sock.close()