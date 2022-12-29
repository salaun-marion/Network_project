import random
import socket
import tqdm  
#nice progress bar with 'tqdm'library
#tqdm means te quiero demasiado ^^
import os
#to set up the path for the file
import sys


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1400
WINDOW_SIZE = 4
#we decrease the size of the buffer to 1400 because it's the size of an ip packet

#ip address of the server & port
host = "127.0.0.1"
port = 12345


#name of the file we want to send and his size
filename = "/Users/marion/Documents/00_BINFO2/3.5.Networks_1/Network_project/SetServerClientFile/scully_hitchcock_brooklyn99.png"
filesize = os.path.getsize(filename)
print(f"{filesize}")

#create the server socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#To etablish the connection
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))
print("[+] Connected.")

#thanks to random.random() in 90% of cases server will send the document

#------- Error system to use after ----
def chance(bytes):
    if random.random() > 0.1:
        s.send(bytes)

#chance(lambda: s.send(f"{filename}{SEPARATOR}{filesize}".encode()))
#-----------
#send the filename and the filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit ="B", unit_scale=True, unit_divisor=1024)

# example for range
# In [24]: list(range(10))
# Out[24]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ACKcounter = 0
frameCounter = 0

with open(filename, "rb") as f :
    while True :
        if frameCounter - ACKcounter < WINDOW_SIZE:
            #read the bytes from the file 
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read and ACKcounter == seqNumber:
                break
            else :
                #s.send(bytes_read+("%.8d"%seqNumber).encode())
                chance(bytes_read+("%.8d"%seqNumber).encode())
                seqNumber+=1
        try :
            s.settimeout(0.001)
            result = s.recv(BUFFER_SIZE)
            if ACKcounter == int(result) :
                ACKcounter += 1
    
        except socket.timeout:
            f.seek(-(seqNumber - ACKcounter)*BUFFER_SIZE,os.SEEK_CUR)
            seqNumber = ACKcounter
                
        progress.update(len(bytes_read))
s.send("EndOfFile".encode())
s.close()