#NOT WORKING AT ALL ^^

import socket 

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',12345))

while True :
    data,addr=sock.recvfrom(4096)
    print(data)

    src = open("/Users/marion/Documents/00_BINFO2/3.5.Networks_1/Network_project/SetServerClientFile/hello.txt", "rb")
    file=bytes(src)

    sock.sendto(src,addr)
