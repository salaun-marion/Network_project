import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#'AF_INET'belongs to the IPV4 family
sock.bind(('127.0.0.1',12345))