#!/bin/bash
export FLASK_APP=streamer.py

host=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')
echo $host

flask run -h $host -p 8000 --with-threads
