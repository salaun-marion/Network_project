import socket
import tqdm
import os
import sys

#ip address of the client & port
host = "127.0.0.1"
port = 12345

#receive 4096 bytes each time
BUFFER_SIZE = 1400
WINDOW_SIZE = 4
SEPARATOR = "<SEPARATOR>"

# arguments received 
idprocess = sys.argv[1]

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#To etablish the connection
print(f"\n[+]---- CLIENT {idprocess} ---- ")
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))
print("[+] Connected.")

# Handshake send
s.send(("Handshake"+idprocess).encode())

#receive file infos
received = s.recv(BUFFER_SIZE)
received = received.decode()
filename, filesize = received.split(SEPARATOR)

#remove absolute path is there is
filename = "[RCV"+idprocess+"]_"+ os.path.basename(filename) 
filesize = int(filesize)

#nice fancy progress bar
progress = tqdm.tqdm(range(filesize), f"ID : {idprocess} is receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

# Go-back-n starts here ----
frameCounter = 0

with open(filename, "wb") as f :
    #'wb': write in binary
    while True :

        bytes_read = s.recv(BUFFER_SIZE+8) 
        if bytes_read == b"EndOfFile" :
            # to stop writing
            break
        seqNumber = int(bytes_read[-8:])
        #print(f"RECEIVER :  seqNumber {seqNumber} | framecounter:{frameCounter}")

        if seqNumber == frameCounter :
            s.send(str(frameCounter).encode())
            frameCounter+=1 
            f.write(bytes_read[:-8])
            progress.update(len(bytes_read))
        else :
            pass
            #print("Ignored.")

s.close()


