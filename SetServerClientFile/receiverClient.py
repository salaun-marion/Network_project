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

#'wb': write in binary
frameCounter = 0
with open(filename, "wb") as f :
    while True :
        bytes_read, address = s.recvfrom(BUFFER_SIZE)
        frameCounter+=1
        s.send("ACK".encode())
        if bytes_read == b"EndOfFile" :
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))


#client_socket.close()

s.close()


