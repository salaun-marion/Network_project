import socket

#TUTO follow from Programming Knowledge (cf sources in README)

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#'AF_INET'belongs to the IPV4 family
#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one datagram and get one reply and then the connection terminates

sock.bind(('127.0.0.1',12345))
# '127.0.0.1': IP address
# 12345 : port number 

while True:
    data,addr=sock.recvfrom(4096)
    print(data)
    # UDP adress will change at the opposite of TCP
    # '4096' : number of bytes provided

    message = bytes(("Hello I am UDP server").encode('utf-8'))
    #convert 'message' in bytes
    sock.sendto(message, addr)