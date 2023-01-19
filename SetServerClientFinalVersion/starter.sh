#!/bin/bash

# Compatible for all scenario

for (( i=1 ; i<=$1 ; i++ ));
do 
    python senderServer.py $i $2 $3 $4 $5 &
    sleep 1
    for (( j=1 ; j<=$2 ; j++ )); 
    do
    (python receiverClient.py $j $4 $5) &
    done
    wait

done
wait

echo "## Md5 Checksum for files received ##"
md5 Client*/*

echo "## Md5 for original file ##"
md5 $3

if (($2 > 2)); then 
    end=`date +%s`

    runtime=$((end-start-$1))

    hours=$((runtime / 3600)); 
    minutes=$(( (runtime % 3600) / 60 )); 
    seconds=$(( (runtime % 3600) % 60 ));
    
    echo "##Runtime: $hours:$minutes:$seconds (hh:mm:ss)" 
fi