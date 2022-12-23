SOURCE :

https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
https://stackoverflow.com/questions/12362542/python-server-only-one-usage-of-each-socket-address-is-normally-permitted
https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3

HOW TO :

1. Install `tqdm` package with this command line in Terminal : `pip3 install tqdm``
2. Then create 2 terminal windows
3. Run in the first terminal this command line `python receiverServer.py`
4. Then run this command line on the other terminal `python senderClient.py`

------ SPECIFITY WINDOWS 10 ----

#IF THE PORT IS OCCUPPIED 

# 12345 is your port number
`netstat -ano|findstr 12345`

# 19088 is the PID of the process
TCP    0.0.0.0:4444      *:*        19088

#THEN WE KILL THE CURRENT PROCESS
`tskill 19088`

#TO INDICATE A PATH ON WINDOWS
filename = r("C:absolutepathblabla...")
# 'r' will convert a normal string to a raw string