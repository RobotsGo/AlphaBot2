# AlphaBot2 - RobotsGo 

## Info
Repo containing all RobotsGo development code for the AlphaBot2 Platform  

### AlphaBot2-Control
Take control of the AlphaBot via gamepad or over a TCP/IP connection with keyboard while   
streaming the AB2 camera via ustreamer to webpage or player.       

For python3 only!!!!!

## Getting started
Set your AlphaBot2 up with Raspberry Pi OS https://www.raspberrypi.org/software/.   
Log in to your AlphaBot2 via your preferred method.      
Download the AlphaBot2-Setup.sh script make it executable and then run the script.   
```
$ cd ~
$ wget -L https://raw.githubusercontent.com/RobotsGo/AlphaBot2/main/AlphaBot2-Setup.sh
$ chmod +x AlphaBot2-Setup.sh
$ ./AlphaBot2-Setup.sh
```
This script will allow you to:    
* Update rpi os, install all needed dependencies, xrdp, clone RobotsGo/AlphaBot2 repo, enable ssh, enable required hardware support, update eeprom   
* Removes un-needed packages, setup Bluetooth XboxOne controller support, download and compile sixpair for PS3 Bluetooth pairing     
* Install all needed dependencies for client network control, clone RobotsGo's AlphaBot2 repo    
* Set the AlphaBot 2 up as a wifi 5Ghz AP with DHCP, WPA, SSID    

### Running AlphaBot2-Control

Launch the start script from ~/AlphaBot2/AlphaBot2-Control/   
```
$ ./start.sh 
```
From this script you can start:      
* ustreamer :Default port 8000    
* Network Controller client      
* Network Controller Server :Default port 5000        
* PS3 Controller Server    
* XboxOne Controller Server    
* MMP1251 Mod My PI Controller Server        
* ipega PG-9099 bluetooth Controller Server    
* View version info and RobotsGo links    

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

ipega PG-9099 'WOLAVERINE' BlueTooth Controller   
Start = Exit, RT = Forwards, LT = Backwards          
RightStick = Steering Left/Right, LeftStick = Camera Up,Down,Left,Right         
D UP/Down = Set Speed modes,  D Left/Right = Change led's colours         
A = Kick, Y = Center Camera, X = Buzzer          


### TO DO
~~Add XboxOne controller support~~
~~Request Add MMP1251 Mod My Pi gamepad support~~   
~~Move as much functions over to the gpiozero library~~   
~~Use the buzzer~~            
~~Logo overlay on video stream~~   
Use the IR sensors   
Share data between the controller application and the streamer application (colour, speed modes)    
~~Get images and videos of unit in action~~       
~~Sort out rpi os install/script for GameHat + AB2~~
~~Improve camera streaming performance - investagate other ways~~ VLC requires 'Network Caching' to be reduced to 200ms to remove delay   
Build all this in to a wiki        
