import random
import socket
import tqdm
import os
import sys

#arguments received 
idprocess = sys.argv[1]
probability = float(sys.argv[2])
window_size = sys.argv[3]

BUFFER_SIZE = 1400
WINDOW_SIZE = window_size
SEPARATOR = "<SEPARATOR>"

#ip address of the client & port
host = "127.0.0.1"
port = 12345

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#To etablish the connection
print(f"\n[+]---- CLIENT {idprocess} ---- ")
print(f"\n[+] Connecting to {host}:{port}")
s.connect((host,port))
print("\n[+] Connected.")

# Handshake send
s.send(("Handshake"+idprocess).encode())

#receive file infos
received = s.recv(BUFFER_SIZE)
received = received.decode()
filename, filesize = received.split(SEPARATOR)

#create the path to store the file
directory = "Download"+idprocess
parent_dir = "/Users/marion/Documents/00_BINFO2/3.5.Networks_1/Network_project/SetServerClientFinalVersion"
path = os.path.join(parent_dir, directory)
try :
    os.mkdir(path)
except FileExistsError : 
    pass

filename = "[RCV"+idprocess+"]_"+ os.path.basename(filename) 
filesize = int(filesize)

#------- Error system ----
def chance(bytes):
    if random.random() > probability:  
        s.send(bytes)
#-----------

#nice fancy progress bar
progress = tqdm.tqdm(range(filesize), f"\nID : {idprocess} is receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

# Go-back-n starts here ----
frameCounter = 0

with open(path+"/"+filename, "wb") as f :
    #'wb': write in binary
    while True :
        bytes_read = s.recv(BUFFER_SIZE+8) 
        if bytes_read == b"EndOfFile" :
            # to stop writing
            break
        seqNumber = int(bytes_read[-8:])
        chance(str(frameCounter).encode())

        if seqNumber == frameCounter :
            frameCounter+=1 
            f.write(bytes_read[:-8])
            progress.update(len(bytes_read))
        else :
            pass

s.close()