#!/bin/bash

#!/bin/sh

start_Client(){
    echo "Start GameHat Client"
    echo python3 gameHatMapping.py -s $server &
    disown
}

start_VLC(){
    echo "Stat VLC and connect to video stream"
    vlc -f http://$server:8000/video_feed
}

launcher_exit() {
    pkill vlc
    exit
}


server=`cat ip.txt`
echo "AlphBot2 streaming and WaveShare GameHat control client version 0.1"
echo "Will try and connect to AlphaBot @: $server"

start_Client
start_VLC
launcher_exit
