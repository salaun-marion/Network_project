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

#-----------
#send the filename and the filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

#start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit ="B", unit_scale=True, unit_divisor=1024)

#Go-Back-N starts here -----
ACKcounter = 0
seqNumber = 0

with open(filename, "rb") as f :
    while True :
        if seqNumber - ACKcounter < WINDOW_SIZE:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read and ACKcounter == seqNumber:
                #to stop the sending
                break
            else :
                #s.send(bytes_read+("%.8d"%seqNumber).encode())
                chance(bytes_read+("%.8d"%seqNumber).encode())
                #encode() transform seqNumber which is `int` into `bytes``
                #seqNumber has the size of 8
                # 1, 2, 3, 4   .... 700 000 : 8 chiffres possibles pour être tranquille
                
                seqNumber+=1
        try :
            s.settimeout(0.01)
            # connected to EstimatedRTT -> something to deepen :) 
            # settimeout function means wait for answer, here wait 0.01 sec
            result = s.recv(BUFFER_SIZE)
            # result = frameCounter already received by the receiver 
            # recv ≠ recfrom
            # same difference as sendto ≠ send

            if ACKcounter == int(result) :
                ACKcounter += 1
    
        except socket.timeout:
            f.seek(-(seqNumber - ACKcounter)*BUFFER_SIZE,os.SEEK_CUR)
            # seek() function allows la "position de la tête de lecture" to be changed into a new position
            # `os.SEEK_CUR` : avoid that the pointer will be BEFORE the beginning of the file
            seqNumber = ACKcounter
                
        progress.update(len(bytes_read))

s.send("EndOfFile".encode())
s.close()