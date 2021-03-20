# AlphaBot2 - RobotsGo 
# GamePad-Control

Drive, Camera, LED lights control via Gamepad

## Getting started
Supported game pads   
XboxOne Wireless Controller via bluetooth https://pimylifeup.com/xbox-controllers-raspberry-pi/  
Steam Controller via dongle or bluetooth
PS3 Controller via bluetooth https://pimylifeup.com/raspberry-pi-playstation-controllers/

D-Pad Up/Down: High Speed, Medium Speed, Low Speed    
D-Pad Left/Right: Change LED Colours off, Red, Green, Blue, White    
Right-Trigger: Move Forward  
Left-Trigger: Move Backwards  
Joy-Right: Steering Left, Right  
Joy-Left: Camera Left, Right, Up, Down  
A: Play burp-sound-effect.mp3  
B: Play Cow-moo-sound.mp3  
X: Play Dj-air-horn-sound-effect.mp3  
Y: Play Duck-quack.mp3  
XBOX: Quit    

## Usage
Script must run as root or LED lights will not work.     
```
$ sudo python main.py -g XboxOne 

Args
-h, --help, Display Help
-c, --camera, Disable mpeg streamer
-g, --gamepad, GamePad you would like to use to control the robot. Options are XboxOne or Steam
-v, --version, See version and build information
```
Onboard Audio and LED's cannot work at the same time as they use the same PWM. See Limitations: https://github.com/jgarff/rpi_ws281x 

Required to play audio mpg123
```
$ sudo apt update
$ sudo apt full-upgrade
$ sudo apt-get install mpg123
```
Required if you to to make sound portable.  
https://www.jaycar.com.au/audio-amplifier-module-with-speaker-for-arduino/p/XC3744   
Needs to be powered by its own power supply, one 18650 cell works well.

Force audio out of Headphone jack.
```
$ sudo echo "hdmi_ignore_edid_audio=1" > /boot/config.txt
$ sudo echo "audio_pwm_mode=2" > /boot/config.txt
$ sudo reboot
``` 
## Issues
* Add support for more gamepads

