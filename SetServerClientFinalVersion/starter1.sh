#!/bin/bash

python senderServer.py $1 &
sleep 1
# python receiverClient.py &
for (( i=1 ; i<=$1 ; i++ )); 
do
    (python receiverClient.py $i) &
done
wait