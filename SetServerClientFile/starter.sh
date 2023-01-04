#!/bin/bash

python senderServer.py &
sleep 2
python receiverClient.py &