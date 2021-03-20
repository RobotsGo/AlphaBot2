# AlphaBot2 - RobotsGo 
# FootBall-Control 

Kick a pingpong ball with you AlphaBot2   

## Getting started
Supported game pads   
XboxOne Wireless Controller via bluetooth https://pimylifeup.com/xbox-controllers-raspberry-pi/  
Steam Controller via dongle or bluetooth  
PS3 Controller via bluetooth https://pimylifeup.com/raspberry-pi-playstation-controllers/  

Needed Parts   
Mini Push-Pull Solenoid - 5V https://www.littlebird.com.au/products/mini-push-pull-solenoid-5v   
5V 1-Channel Relay Board Module https://www.littlebird.com.au/products/5v-1-channel-relay-board-module  
3d Print kickerV2.stl in printableParts  
3d Print 18650SupportV1.stl in printableParts  
18650 Battery, Battery Holder and two small self tappers   

## Usage

Print 3d parts
Fit kickerV2 to the front bottom board by removing, and using the mounting's screws of the front board ball support.    
Fit 18650Support to the top circuit board, joystick side.   

Using the Ultrasonic module interface pins 5V, GND, TRIG connect to (+), (-), (S) pins of the relay   
18650 (-) -> to (COM) of Realy   
Relay (NO) -> Solenoid   
Solenoid -> 18650 (+)   

Script must run as root or LED lights will not work.     
```
$ sudo python main.py -g XboxOne -t blue 

Args
-c, --camera, Disable mpeg streamer
-g, --gamepad, GamePad you would like to use to control the robot. Options are XboxOne, Steam or PS3
-t, --team, Set the Robot's team colour. Options are blue or red.
-v, --version, See version and build information
```
## Issues
* Add support for more gamepads
* Get some images/videos of the robots in action 
* Finalise wiring and create wiring diagram 
* When final version is completed, develop an assembly guide 
