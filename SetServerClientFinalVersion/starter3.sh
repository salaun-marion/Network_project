#!/bin/bash

# scenario 3 : send to each client (up to 6), 1 file of up to 300Mb

start=`date +%s`

for (( i=1 ; i<=1 ; i++ ));
do 
    python senderServer.py $i 6 300Mb_Libreoffice.dmg 0.1 3 &
    sleep 1
    for (( j=1 ; j<=6 ; j++ )); 
    do
    (python receiverClient.py $j 0.1 3) &
    done
    wait

done
wait
end=`date +%s`

echo "## Md5 Checksum for files received ##"
md5 Client*/*

echo "## Md5 for original file ##"
md5 300Mb_Libreoffice.dmg

runtime=$((end-start-1))

hours=$((runtime / 3600)); 
minutes=$(( (runtime % 3600) / 60 )); 
seconds=$(( (runtime % 3600) % 60 ));

echo "##Runtime without Md5 checking: $hours:$minutes:$seconds (hh:mm:ss)" 
