#!/bin/bash

python senderServer.py &
sleep 2

for n in {1..$1};
do

    python receiverClient.py &
done