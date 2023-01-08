#!/bin/bash

# 1st scenario : sending to 2 client 1GB of file

for (( i=1 ; i<=1 ; i++ ));
do 
    python senderServer.py $i 2 1GB.mkv 0.1 4 &
    sleep 1
    for (( j=1 ; j<=2 ; j++ )); 
    do
    (python receiverClient.py $j 0.1 4 ) &
    done
    wait
done

echo "## Md5 Checksum for files received ##"
md5 Down*/*

echo "## Md5 for original file ##"
md5 1GB.mkv