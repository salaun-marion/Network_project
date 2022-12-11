import socket
import tqdm  
#nice progress bar with 'tqdm'library
#tqdm means te quiero demasiado ^^
import os
#to set up the path for the file

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

#ip address of the server & port
host = "127.0.0.1"
port = 12345

#name of the file we want to send and his size
filename = "/Users/marion/Documents/00_BINFO2/3.5.Networks_1/Network_project/SetServerClientFile2/hello.txt"
filesize = os.path.getsize(filename)
print(f"{filesize}")

#create the client socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#To etablish the connection
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))
print("[+] Connected.")

#send the filename and the filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit ="B", unit_scale=True, unit_divisor=1024 )
# example for range
# In [24]: list(range(10))
# Out[24]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


with open(filename, "rb") as f:
    while True :
        #read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.send("bloubli".encode())
s.close()