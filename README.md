# AlphaBot2 - RobotsGo 

## Notes
Repo containing original Waveshare AlphaBot2 demo code and updates/fixes as needed.   
Link to original sources https://www.waveshare.com/w/upload/7/74/AlphaBot2.tar.gz

AlphaBot2 wiki https://www.waveshare.com/wiki/AlphaBot2-Pi

Also original development for the AlphaBot2 platform by members of RobotGo.

## Getting started
Once you AlphaBot2 is all setup with Raspberry Pi OS.

Update your pi to the latest Raspberry Pi OS.
```
$ sudo apt update
$ sudo apt full-upgrade
```

Install needed dependencies from the Raspberry Pi OS repos. 
```
$ sudo apt-get install ttf-wqy-zenhei
$ sudo apt-get install python-pip
$ sudo apt-get install cmake libjpeg8-dev
$ sudo apt-get install gcc g++
$ sudo apt-get install python-smbus
$ sudo apt-get install python-serial
$ sudo apt-get install build-essential python-dev scons swig -y
$ sudo apt-get install python-bottle -y
$ sudo pip install RPi.GPIO
$ sudo pip install spidev
$ sudo reboot
```
Clone: rpi_ws281x, build and install.
```
$ cd /home/pi
$ git clone https://github.com/jgarff/rpi_ws281x.git
$ sudo /home/pi/rpi_ws281x/scons
```
Clone: mjpg-streamer, build and install.
```
$ cd /home/pi
$ git clone https://github.com/jacksonliam/mjpg-streamer.git
$ cd /home/pi/mjpg-streamer/mjpg-streamer-experimental
$ make
$ sudo make install
```
Clone: PiBorg GamePad Library
```
$ cd /home/pi
$ git https://github.com/RobotsGo/Gamepad.git
```
Clone: RobotsGo AlphaBot2 repo
```
$ cd /home/pi
$ git clone https://github.com/RobotsGo/AlphaBot2.git
```
Start Service: mjpg-streamer
```
$ cd /home/pi
$ sudo cp /home/pi/AlphaBot2/Scripts/mjpgstreamer.service /lib/systemd/system/mjpgstreamer.service
$ sudo chmod 644 mjpgstreamer.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable mjpgstreamer.service
$ sudo systemctl start mjpgstreamer.service
```
