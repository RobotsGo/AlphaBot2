# AlphaBot2 - RobotsGo 
# GamePad-Control

Drive, Camera, LED lights control via Gamepad

## Getting started
Supported game pads   
XboxOne Wireless via blutooth https://pimylifeup.com/xbox-controllers-raspberry-pi/   

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
Script must run as root as sound will not work or the LED lights.

## Issues
* Sound system (pulse Audio) can only play audio first run of the script, any runs of the script after, sound is distorted a reboot is required to restore sound.   
* Pulseaudio or alsa not releasing @ script exit.  
* pi user is part of audio group and playing audio as user works but not with-in the script.
* Trying to init devices on batteries will make the pi reboot as too much drain at once (added some time.sleep(5) during init process).
* Add more support for gamepads, with a simple args to select at script start.

