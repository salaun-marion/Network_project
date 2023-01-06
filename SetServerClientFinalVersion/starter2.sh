#!/bin/bash

# scenario 2 : send to each client (up to 10), 10 files of at least 50 Mb for each

for (( i=1 ; i<=10 ; i++ ));
do 
    python senderServer.py 10 $i &
    sleep 1
    for (( j=1 ; j<=10 ; j++ )); 
    do
    (python receiverClient.py $j) &
    done
    wait
done