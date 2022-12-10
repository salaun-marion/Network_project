import socket
import tqdm  
#nice progress bar with 'tqdm'library
# tqdm means te quiero demasiado ^^
import os
# DK (=don't know why it's here) interest to import os library ?

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

#ip address of the server & port
host = "192.168.1.101"
port = 5001

#name of the file we want to send and his size
filename = "hello.txt"
filesize = os.path.getsize(filename)

#create the client socket
s = socket.socket()

#To etablish the connection
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print(f"[+] Connected")

#send the filename and the filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit ="B", unit_scale=True, unit_divisor=1024 )

with open(filename, "rb") as f:
    while True :
        #read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))

s.close()