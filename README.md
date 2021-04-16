# AlphaBot2 - RobotsGo 

## Info
Repo containing all RobotsGo development code for the AlphaBot2 Platform  

### AlphaBot2-Control
Take control of the AlphaBot via gamepad or over a TCP/IP connection with keyboard while   
streaming the AB2 camera with openCV support.    

For python3 only!!!!!

## Getting started - AlphaBot
Once your AlphaBot2 is all setup with Raspberry Pi OS.

Update your pi to the latest Raspberry Pi OS.
```
$ sudo apt update
$ sudo apt full-upgrade
```
Install needed dependencies. 
```
$sudo apt install python-gpiozero
$sudo pip3 install opencv-python 
$sudo pip3 install flask
$sudo pip3 install rpi_ws281x
$sudo pip3 install adafruit-circuitpython-servokit
$sudo pip3 install psutil
$sudo pip3 install imutils
$sudo pip3 install numpy
$sudo pip3 install pynput
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
$ chmod +x startGameHatClient.sh
```
Then Launch the start script    
```
$ ./start.sh 
```
From this script you can start:      
FLASK/OpenCV streammer :Default port 8000    
Network Controller client      
Network Controller Server :Default port 5000        
PS3 Controller Server    
XboxOne controller Server    
MMP1251 Mod My PI controller Server   
View version info and RobotsGo links    

Streamer and Network Controller Server will auto set the IP of the AlphaBot     
When script exits the Streamer should stop

### Controller support   
PS3 Controller      
https://pimylifeup.com/raspberry-pi-playstation-controllers/        
R2 = Forwards,  L2 = Backwards, RightStick = Steering Left/Right         
LeftStick = Camera Up,Down,Left,Right,  Cross = Kicker            
Triangle = Center Camera, D UP/Down = Set Speed modes         
D Left/Right = Change led's colours, Square = Buzzer       
PS = Exit            

XboxOne Controller    
https://pimylifeup.com/xbox-controllers-raspberry-pi/      
xbox = Exit, RT = Forwards, LT = Backwards       
RightStick = Steering Left/Right, LeftStick = Camera Up,Down,Left,Right      
D UP/Down = Set Speed modes,  D Left/Right = Change led's colours      
A = Kick, Y = Center Camera, X = Buzzer       

Mod My Pi (mmp1251) Controller      
R2 = Forwards,  L2 = Backwards, HomeButton = exit          
RightStick = Steering Left/Right, A = kicker       
Y = Center Camera, X = Buzzer,  D UP/Down = Set Speed modes         
D Left/Right = Change led's colours, LeftStick = Camera Up,Down,Left,Right      

WaveShare rpi GameHat      
Start = exit,  Select = Center Camera,  TR = kick         
X = Forwards, B = Backwards,  Y = Left         
A = Right,  LeftStick = Camera Up,Down,Left,Right      

Keyboard - Network client   
Arrow Keys = Forwards, Backwards, Left, Right, Space = Kicker         
wasd = Camera Up,Down,Left,Right, q = Centre Camera         
1 2 3 = Speed Modes,   ,. = Change led's colours,  e = Buzzer     

## Getting started - Wave Share GAME HAT   
Downlaod and install latest RetroPie   
https://retropie.org.uk/download/   
Setup SSH   
https://retropie.org.uk/docs/SSH/   
Update RetroPie setup script/RetroPie and underlying rpi os   
https://retropie.org.uk/docs/Updating-RetroPie/   
https://www.raspberrypi.org/documentation/raspbian/updating.md     
Follow the Wave Share Game Hat wiki to setup screen and follow the retropie-v4.7 install instructions        
https://www.waveshare.com/wiki/Template:Game_HAT_User_Manual     
Install PIXEL DE   
https://www.crackedconsole.com/2019/04/18/installing-pixel-desktop-environment-on-retropie-for-raspberry-pi/     
Install needed dependencies. 
```
$sudo apt install python-gpiozero
$sudo apt install xrdp
$sudo apt install python3-pip
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
$ chmod +x startGameHatClient.sh
```
Then Launch the start script on the AlphaBot2 and select  "Menu Option 3: Start Network Server"         
```
$ ./start.sh
```
On the Game Hat edit ip.txt and enter the ip address for the AlphaBot2   
Then Launch
```
$ ./startGameHatClient.sh
```


### TO DO
~~Add XboxOne controller support~~
~~Request Add MMP1251 Mod My Pi gamepad support~~   
~~Move as much functions over to the gpiozero library~~   
~~Use the buzzer~~            
~~Logo overlay on video stream~~   
Use the IR sensors   
Share data between the controller application and the streamer application (colour, speed modes)    
Get images and videos of unit in action       
Sort out rpi os install/script for GameHat + AB2   
Remove the semi transparent effect on the opencv overlay   
Build all this in to a wiki   
