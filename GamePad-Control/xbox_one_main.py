#!/usr/bin/env python
#coding: utf-8

# Written by spoonie (Rick Spooner) for RobotsGo 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




import sys, os, signal 
sys.path.insert(0, "/home/pi/Gamepad")
sys.path.insert(1, "/home/pi/AlphaBot2/python")

#################### Import libaries ####################
import Gamepad
import time
import subprocess
from AlphaBot2 import AlphaBot2
from PCA9685 import PCA9685
from rpi_ws281x import Color, PixelStrip, ws
import RPi.GPIO as GPIO

#################### Set some initial state ####################
global running
running = True

global SELECTED_COLOUR
SELECTED_COLOUR = 0

global SPEED_MODE
SPEED_MODE = 1

alphaBot2 = AlphaBot2()


#################### Led Settings ####################
    # LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP = ws.SK6812_STRIP
COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.setBrightness(50)
strip.begin()

print('LED lights setup')
print('Wait 5sec for power to stabilise if running on Batteries')
time.sleep(5)

#################### Speed settings ####################
    #If robot wont go straight fine tune PWM of motors
    #Looking from the front, PWMA is on the right.
LOW_SPEED_PWMA =  30
LOW_SPEED_PWMB =  30
MEDIUM_SPEED_PWMA =  50
MEDIUM_SPEED_PWMB =  50
HIGH_SPEED_PWMA   =  80
HIGH_SPEED_PWMB   =  80

print('Speed settings set')
#################### Gamepad settings ####################

gamepadType = Gamepad.XboxONE
buttonExit = 'HOME'
triggerForwards = 'RT'
triggerBackwards = 'LT'
steering = 'RAS -X'
cameraVertical = 'LAS -Y'
cameraHorizontal = 'LAS -X'
adjustSpeed = 'DPAD -Y'
changeColour = 'DPAD -X'
playSound1 = 'A'
playSound2 = 'B'
playSound3 = 'X'
playSound4 = 'Y'
pollInterval = 0.1

#################### Servo settings ####################
pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

    #Set the Horizontal servo parameters
horizontalPulse = 1500  #Sets the initial Pulse
horizontalStep = 0      #Sets the initial step length

    #Set the vertical servo parameters
verticalPulse = 1500  #Sets the initial Pulse
verticalStep = 0      #Sets the initial step length

pwm.setServoPulse(1,verticalPulse)
pwm.setServoPulse(0,horizontalPulse)   

print('Servo settings set')
print('Wait 5sec for power to stabilise if running on Batteries')
time.sleep(5)
#################### Functions ####################
def exitApp():
    
    strip.setPixelColor(0, Color(0, 0, 0, 0)) #None
    strip.setPixelColor(1, Color(0, 0, 0, 0))
    strip.setPixelColor(2, Color(0, 0, 0, 0))
    strip.setPixelColor(3, Color(0, 0, 0, 0))
    strip.show()
    
    print('Lights off')
    
    print('EXIT, quitting script')
    
    gamepad.disconnect()
    print('Gamepad disconnected')
    
    running = False
    print('Running set to false')
    
    try:
        name = 'mpg123'
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):  
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL) 
        print('All instances of mpg123 have been killed')
     
    except: 
        print("Error Encountered while running script")
        
    print("Wait for a bit")
    time.sleep(5)
        
    print('Exit')
    sys.exit()

        
def setColour():

    try:
        if (SELECTED_COLOUR == 0):
                strip.setPixelColor(0, Color(0, 0, 0, 0)) #None
                strip.setPixelColor(1, Color(0, 0, 0, 0))
                strip.setPixelColor(2, Color(0, 0, 0, 0))
                strip.setPixelColor(3, Color(0, 0, 0, 0))
                strip.show()
                
        elif (SELECTED_COLOUR == 1):
                strip.setPixelColor(0, Color(255, 0, 0)) #Red
                strip.setPixelColor(1, Color(255, 0, 0))
                strip.setPixelColor(2, Color(255, 0, 0))
                strip.setPixelColor(3, Color(255, 0, 0))
                strip.show()
        
        elif (SELECTED_COLOUR == 2):
                strip.setPixelColor(0, Color(0, 255, 0)) #Green
                strip.setPixelColor(1, Color(0, 255, 0))
                strip.setPixelColor(2, Color(0, 255, 0))
                strip.setPixelColor(3, Color(0, 255, 0))
                strip.show()
        
        elif (SELECTED_COLOUR == 3):
                strip.setPixelColor(0, Color(0, 0, 255)) #Blue
                strip.setPixelColor(1, Color(0, 0, 255))
                strip.setPixelColor(2, Color(0, 0, 255))
                strip.setPixelColor(3, Color(0, 0, 255))
                strip.show()
        
        elif (SELECTED_COLOUR == 4):
                strip.setPixelColor(0, Color(255, 255, 255,)) #White
                strip.setPixelColor(1, Color(255, 255, 255,))
                strip.setPixelColor(2, Color(255, 255, 255,))
                strip.setPixelColor(3, Color(255, 255, 255,))
                strip.show()
                
    except Exception as e:
            print e.message
        
def setSpeed():
    
    if (SPEED_MODE == 1):
        alphaBot2.setPWMA(LOW_SPEED_PWMA);
        alphaBot2.setPWMB(LOW_SPEED_PWMB);

    elif(SPEED_MODE == 2):
        alphaBot2.setPWMA(MEDIUM_SPEED_PWMA);
        alphaBot2.setPWMB(MEDIUM_SPEED_PWMB);
        
    elif(SPEED_MODE == 3):
        alphaBot2.setPWMA(HIGH_SPEED_PWMA);
        alphaBot2.setPWMB(HIGH_SPEED_PWMB);
        
    else:
        alphaBot2.setPWMA(LOW_SPEED_PWMA);
        alphaBot2.setPWMB(LOW_SPEED_PWMB);
        

def playMp3(path):

    try:
        subprocess.Popen(['mpg123', '-q', path])
        
    except Exception as e:
                print e.message	
            
def cameraMovment():
	global horizontalPulse,verticalPulse,horizontalStep,verticalStep,pwm
	
	if(horizontalStep != 0):
		horizontalPulse += horizontalStep
		if(horizontalPulse >= 2500): 
			horizontalPulse = 2500
		if(horizontalPulse <= 500):
			horizontalPulse = 500
		pwm.setServoPulse(0,horizontalPulse)    
		
	if(verticalStep != 0):
		verticalPulse += verticalStep
		if(verticalPulse >= 2500): 
			verticalPulse = 2500
		if(verticalPulse <= 500):
			verticalPulse = 500
		pwm.setServoPulse(1,verticalPulse)

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected, setup complete') 

# Create some callback functions for single events
def playSound1Pressed(): #burp-sound-effect.mp3
    print('Playing burp-sound-effect.mp3')
    playMp3('/home/pi/AlphaBot2/GamePad-Control/burp-sound-effect.mp3')
    

def playSound2Pressed(): #Cow-moo-sound.mp3
    print('Playing Cow-moo-sound.mp3')
    playMp3('/home/pi/AlphaBot2/GamePad-Control/Cow-moo-sound.mp3')
    

def playSound3Pressed(): #Dj-air-horn-sound-effect.mp3
    print ('Playing Dj-air-horn-sound-effect.mp3')
    playMp3('/home/pi/AlphaBot2/GamePad-Control/Dj-air-horn-sound-effect.mp3')
    
    
def playSound4Pressed(): #Duck-quack.mp3
    print('Playing Duck-quack.mp3') 
    playMp3('/home/pi/AlphaBot2/GamePad-Control/Duck-quack.mp3')
    
def exitButtonPressed():
    exitApp()
        
# Start the background updating
gamepad.startBackgroundUpdates()

# Register the callback functions
gamepad.addButtonPressedHandler(playSound1, playSound1Pressed)
gamepad.addButtonReleasedHandler(playSound2, playSound2Pressed)
gamepad.addButtonReleasedHandler(playSound3, playSound3Pressed)
gamepad.addButtonReleasedHandler(playSound4, playSound4Pressed)
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)

# Joystick events handled in the background
try:
    while running and gamepad.isConnected():
    
        if gamepad.axis(triggerBackwards) == 1:
            print('Backwards')
            alphaBot2.backward();
            
        elif gamepad.axis(triggerForwards) == 1:
            print('Forwards')
            alphaBot2.forward();
            
        elif gamepad.axis(steering) == 1:
            print('Right') 
            alphaBot2.right();
            
        elif gamepad.axis(steering) == -1:
            print('Left')
            alphaBot2.left();
            
        elif gamepad.axis(cameraVertical) == -1:
            verticalStep = -10
            print('Camera UP ') 
            cameraMovment();
            
        elif gamepad.axis(cameraVertical) == 1:
            verticalStep = 10
            print('Camera Down ')
            cameraMovment();
            
        elif gamepad.axis(cameraHorizontal) == -1:
            horizontalStep = 10
            print('Camera Left ')
            cameraMovment();
            
        elif gamepad.axis(cameraHorizontal) == 1:
            horizontalStep = -10
            print('Camera Right ')
            cameraMovment();
        
        elif gamepad.axis(adjustSpeed) == -1:
            if SPEED_MODE < 3:
                SPEED_MODE = (SPEED_MODE + 1) 
                setSpeed()
                print('Speed mode ' + str(SPEED_MODE)) 
            
            else:
                print('Speed mode ' + str(SPEED_MODE))
                
        elif gamepad.axis(adjustSpeed) == 1:
            if SPEED_MODE > 1:
                SPEED_MODE = (SPEED_MODE - 1)
                setSpeed() 
                print('Speed mode ' + str(SPEED_MODE))
            
            else:
                print('Speed mode ' + str(SPEED_MODE))  
                
        elif gamepad.axis(changeColour) == 1:
            if  SELECTED_COLOUR < 4:
                SELECTED_COLOUR = (SELECTED_COLOUR + 1)
                setColour()
                print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR)) 
            
            else:
                print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
            
        elif gamepad.axis(changeColour) == -1:
            if SELECTED_COLOUR > 0:
                SELECTED_COLOUR = (SELECTED_COLOUR - 1)
                setColour() 
                print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
            else:
                print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))  
        
        else:
            horizontalStep = 0
            verticalStep = 0
            alphaBot2.stop();
        
        time.sleep(pollInterval)
        
except Exception as e:
        print e.message
        

        
    
    




