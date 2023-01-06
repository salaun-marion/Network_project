#!/bin/bash

# 1st scenario : sending to 2 client 1GB of file

python senderServer.py 1 0 &
sleep 1

for (( i=1 ; i<=1 ; i++ )); 
do
    (python receiverClient.py $i) &
done
wait