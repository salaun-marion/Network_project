------- HOW TO RUN OUR PROGRAM------
This program works with python so please check if it's already installed .
This program was tested on Mac OS 13.1. 
For Windows please see special section below.

1. Install `tqdm` package with this command line : `pip3 install tqdm`
2. Allows the script to run `chmod u+x nameofscript.sh``
3. Run the script : `./nameofscript.sh`

#### Table of arguments for starter.sh ####

### => For Server ###
# number_of_client        $2             
# filename                $3        
# probability             $4        
# window_size             $5        

### => For Client ###
# number_of_client        $2       
# probability             $4        

****** WINDOWS 10 ******

#IF THE PORT IS OCCUPPIED 

    # 12345 is your port number
    `netstat -ano|findstr 12345`

    # 19088 is the PID of the process
    TCP    0.0.0.0:4444      *:*        19088

#THEN WE KILL THE CURRENT PROCESS
`tskill 19088`

#TO INDICATE A PATH ON WINDOWS
filename = r("C:absolutepath...")
# 'r' will convert a normal string to a raw string


------- SOURCES ------

Tutorial about how to create a TCP connection :
https://www.thepythoncode.com/article/send-receive-files-using-sockets-python

Problems encounters with Windows 10 : 
- port occupied : https://stackoverflow.com/questions/12362542/python-server-only-one-usage-of-each-socket-address-is-normally-permitted
- windows path needs r : https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3

How to create argument system for CLI :
https://www.youtube.com/watch?v=QJBVjBq4c7E

Go-Back-N : 
- https://www.baeldung.com/cs/networking-go-back-n-protocol
- https://www.youtube.com/watch?v=QD3oCelHJ20

Bash script : 
- executed process at the same time : https://stackoverflow.com/questions/39452132/how-to-start-2-programs-that-need-separate-terminals-from-a-bash-script
- how to get running time of a process with bash : https://unix.stackexchange.com/questions/52313/how-to-get-execution-time-of-a-script-effectively 


****** WINDOWS 10 ******

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