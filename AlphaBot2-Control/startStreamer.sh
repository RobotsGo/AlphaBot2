#!/bin/bash

host=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')
echo $host

ustreamer --format=YUYV --brightness=55 --encoder=omx --workers=3 --persistent --drop-same-frames=30 --host=$host --port=8000 
