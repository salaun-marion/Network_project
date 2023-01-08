import random
import socket
import tqdm  
import os
import sys

#ARGUMENTS
nbServer = sys.argv[1]
nbClient = sys.argv[2]

#name of the file we want to send
filename = sys.argv[3]
#filename = "1Gb.mkv"
#filename = "50Mb.zip"
#filename = "readme.txt"
#filename = "scully_hitchcock_brooklyn99.png"

#probability = float(sys.argv[4])
probability = 0.1

window_size = int(sys.argv[5])

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1400
#WINDOW_SIZE = window_size
WINDOW_SIZE = 4
#we decrease the size of the buffer to 1400 because it's the size of an ip packet

# IP address and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 12345

#size of the file
filesize = os.path.getsize(filename)

#create the server socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#'bind()'has only one argument possible : so we do a tuple (,) and we give to bind
s.bind((SERVER_HOST,SERVER_PORT))
print(f"\n[*]########## SERVER ##########")
print(f"\n[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#Handshake reception - dictionnary in python
handSMap = {}
for i in range (0, int(nbClient)) :
    handshake, address = s.recvfrom(BUFFER_SIZE)
    handSMap[address]= 0

#thanks to random.random() in 90% of cases server will send the document
#------- Error system ----
def chance(bytes):
    if random.random() > probability : 
    #if True : 
        for address in handSMap.keys() :     
            s.sendto(bytes, address)
#-----------
#send the filename and the filesize
for address in handSMap.keys() :     
    print(f"{filename}")
    s.sendto(f"{nbServer}_{filename}{SEPARATOR}{filesize}".encode(),address)

#nice fancy bar for progression
progress = tqdm.tqdm(range(filesize), f"\nSending {filename}", unit ="B", unit_scale=True, unit_divisor=1024)

#---- Go-Back-N starts here -----

#Now we have changed ACK counter = handSMap.values()
#'min(handSMap.values())' means the lowest ACK number in the window size
seqNumber = 0

def windowsClosed(seq) :
    for ACK in handSMap.values() :   
        if seq != ACK : 
            return False
    return True

with open(filename, "rb") as f :
    while True :
      
        if seqNumber - min(handSMap.values()) < WINDOW_SIZE:
            bytes_read = f.read(BUFFER_SIZE)
            if bytes_read :
                chance(bytes_read+("%.8d"%seqNumber).encode())
                seqNumber+=1
            elif windowsClosed(seqNumber) :
                break
                #to stop the sending
        try :
            s.settimeout(0.001)
            # settimeout function means wait for answer, here wait 0.001 sec
            result, address = s.recvfrom(BUFFER_SIZE)
            if handSMap[address] <= int(result) :
                # if the ACK is not received we will keep the previous value
                handSMap[address] = int(result)
                
        except socket.timeout:
            f.seek((min(handSMap.values())*BUFFER_SIZE),os.SEEK_SET)
            #os.SEEK_SET means 'set it to the beginning'
            seqNumber = min(handSMap.values())  
        progress.update(len(bytes_read))

for address in handSMap.keys() : 
    s.sendto("EndOfFile".encode(), address)
s.close()
print(f"\n---END---")