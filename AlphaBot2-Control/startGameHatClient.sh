server=`cat ip.txt`
echo "AlphBot2 streaming and WaveShare GameHat control client version 0.1"
echo "Will try and connect to AlphaBot @: $server"

echo "Stat VLC and connect to video stream" 
cvlc -f 'http://'$server':8000/video_feed' & 

echo "Start GameHat Client"
python3 gameHatMapping.py -s $server

pkill vlc

echo "exit"


