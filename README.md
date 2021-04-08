# AlphaBot2 - RobotsGo 

## Info
Repo containing all RobotsGo development code for the AlphaBot2 Platform  

### AlphaBot2-Control
Take control of the AlphaBot via gamepad or over a TCP/IP connection with keyboard while   
streaming the AB2 camera with openCV support.    

For python3 only!!!!!

## Getting started
Once your AlphaBot2 is all setup with Raspberry Pi OS.

Update your pi to the latest Raspberry Pi OS.
```
$ sudo apt update
$ sudo apt full-upgrade
```
Install needed dependencies. 
```
$sudo apt install python-gpiozero
$pip3 install opencv-python 
$pip3 install flask
$pip3 install rpi_ws281x
$pip3 install adafruit-circuitpython-servokit
$pip3 install psutil

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
### Running AlphaBot2-Control
From the AlphaBot2-Control directory 
```
$ chmod +x start.sh
$ chmod +x startStreamer.sh
```
Then start the Launch Script    
```
$ ./start.sh 
```
From this script you can start:      
FLASK/OpenCV streammer :Default port 8000    
Network Controller client
Network Controller Server :Default port 5000    
PS3 Controller Server         
View version info and RobotsGo links

Streamer and Network Controller Server will auto set the IP of the AlphaBot     
When script exits the Streamer should stop

### Controller support
PS3 Controller

https://pimylifeup.com/raspberry-pi-playstation-controllers/   
R1 = Forwards   R2 = Backwards   
RightStick = Steering Left, Right   LeftStick = Camera Up,Down,Left,Right   
Cross = Kicker solenoid   Triangle = Center Camera   
D UP/Down = Set Speed modes   D Left/Right = Change led's colours   

Keyboard

Arrow Keys = Forwards, Backwards, Left, Right   Space = Kicker solenoid   
wasd = Camera Up,Down,Left,Right    q = Centre Camera   
1 2 3 = Speed Modes   ,. = Change led's colours   

### TO DO
Add XboxOne controller support   
Move as much functions over to the gpiozero library   
Use the buzzer   
Use the IR sensors   
Share data between the controller application and the streamer application (colour speed mode)    
Get images and videos os unit in action       
