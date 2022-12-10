import socket
import tqdm
import os

# IP address and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

#receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

#accept connection if there is any
client_socket, address = s.accept()
print(f"[+] {address} is connected.")


#receive file infos
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

#remove absolute path is there is
filename = os.path.basename(filename)
filesize = int(filesize)

#start receiving file from socket
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

#'wb'= write in binary
with open(filename, "wb") as f :
    while True :
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
s.close()


