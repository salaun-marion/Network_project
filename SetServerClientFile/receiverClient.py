import socket
import tqdm
import os

# IP address and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 12345

#receive 4096 bytes each time
BUFFER_SIZE = 1400
WINDOW_SIZE = 4
SEPARATOR = "<SEPARATOR>"

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#'bind()'has only one argument possible : so we do a tuple ( , ) and we give to bind
# same difference as 'print(x,y)' and 'print((x,y))'
s.bind((SERVER_HOST,SERVER_PORT))

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#receive file infos
received, addr = s.recvfrom(BUFFER_SIZE)
received = received.decode()
filename, filesize = received.split(SEPARATOR)

#remove absolute path is there is
filename = os.path.basename(filename) + ".rcv"
filesize = int(filesize)

#start receiving file from socket
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

# Go-back-n starts here ----
frameCounter = 0

with open(filename, "wb") as f :
    #'wb': write in binary
    while True :

        bytes_read, address = s.recvfrom(BUFFER_SIZE+8) 
        if bytes_read == b"EndOfFile" :
            # to stop writing
            break
        # we separate "seqNumber" from the rest of the buffer
        # `-` means reading from right to left
        # Example from ipython
        # In [4]: x
        # Out[4]: b'aedfgh'
        # In [5]: x[-1:]
        # Out[5]: b'h'
        seqNumber = int(bytes_read[-8:])

        if seqNumber == frameCounter :
            s.sendto(str(frameCounter).encode(), address)
            # s = socket
            # sendto ≠ send
            # sendto : send bytes (str(frameCounter).encode()) to this `address`
            # first i converted framecounter to string with str, then to bytes with encode() 
            frameCounter+=1 
            f.write(bytes_read[:-8])
            progress.update(len(bytes_read))
        else :
            print("Error from receiver side.")

s.close()


