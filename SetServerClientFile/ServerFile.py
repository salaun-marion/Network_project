#NOT WORKING AT ALL ^^

import socket 

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('127.0.0.1',12345))

while True :
    data,addr=server.recvfrom(4096)
    print(data)

    src = open("/Users/marion/Documents/00_BINFO2/3.5.Networks_1/Network_project/SetServerClientFile/hello.txt", "rb")
    file= bytes(src)

    server.sendto(src,addr)
