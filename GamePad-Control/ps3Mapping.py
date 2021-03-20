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

import sys, os
sys.path.insert(0, "/home/pi/Gamepad")
sys.path.insert(1, "/home/pi/AlphaBot2/python")

import Gamepad
import time
import led
import speed
import servo
#import audio
from AlphaBot2 import AlphaBot2

global running
running = True

def increaseSpeed():
	global SPEED_MODE
	if SPEED_MODE < 3:
		SPEED_MODE = (SPEED_MODE + 1) 
		setSpeed()
		print('Speed mode ' + str(SPEED_MODE))
	
	else:
		print('Speed mode ' + str(SPEED_MODE))

def decreaseSpeed():
	global SPEED_MODE
	if SPEED_MODE > 1:
		SPEED_MODE = (SPEED_MODE - 1)
		setSpeed() 
		print('Speed mode ' + str(SPEED_MODE))
            
	else:
		print('Speed mode ' + str(SPEED_MODE))  

def increaseColours():
	global SELECTED_COLOUR
	global COLOURS
	if SELECTED_COLOUR < 4:
		SELECTED_COLOUR = (SELECTED_COLOUR + 1)
		led.setColour(SELECTED_COLOUR)
		print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR)) 
            
	else:
		print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))

def decreaseColours():
	global SELECTED_COLOUR
	global COLOURS
	if SELECTED_COLOUR > 0:
		SELECTED_COLOUR = (SELECTED_COLOUR - 1)
		led.setColour(SELECTED_COLOUR) 
		print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
	else:
		print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))  	

def sound1ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundOne()

def sound2ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundTwo()

def sound3ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundThree()

def sound4ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundFour()

def setSpeed():
    
    if (SPEED_MODE == 1):
        alphaBot2.setPWMA(speed.LOW_SPEED_PWMA);
        alphaBot2.setPWMB(speed.LOW_SPEED_PWMB);

    elif(SPEED_MODE == 2):
        alphaBot2.setPWMA(speed.MEDIUM_SPEED_PWMA);
        alphaBot2.setPWMB(speed.MEDIUM_SPEED_PWMB);
        
    elif(SPEED_MODE == 3):
        alphaBot2.setPWMA(speed.HIGH_SPEED_PWMA);
        alphaBot2.setPWMB(speed.HIGH_SPEED_PWMB);
        
    else:
        alphaBot2.setPWMA(speed.LOW_SPEED_PWMA);
        alphaBot2.setPWMB(speed.LOW_SPEED_PWMB);

def exitButtonPressed():
    global running
    running = False

def ps3MappingStart():
    
    global SPEED_MODE
    SPEED_MODE = 1
    
    global SELECTED_COLOUR
    SELECTED_COLOUR = 0
    
    global COLOURS
    COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']
    
    global alphaBot2
    alphaBot2 = AlphaBot2()
    
    gamepadType = Gamepad.PS3
    buttonExit = 'PS'
    triggerForwards = 'R2'
    triggerBackwards = 'L2'
    steering = 'RIGHT-X'
    cameraVertical = 'LEFT-Y'
    cameraHorizontal = 'LEFT-X'
    adjustSpeedUp = 'DPAD-UP'
    adjustSpeedDown = 'DPAD-DOWN' 
    changeColourUp = 'DPAD-RIGHT'
    changeColourDown = 'DPAD-LEFT'
    playSound1 = 'CROSS'
    playSound2 = 'CIRCLE'
    playSound3 = 'SQUARE'
    playSound4 = 'TRIANGLE'
    pollInterval = 0.1

    if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)
    gamepad = gamepadType()
    print('Gamepad connected, setup complete') 
    
# Start the background updating
    gamepad.startBackgroundUpdates()
    gamepad.addButtonPressedHandler(adjustSpeedUp, increaseSpeed)
    gamepad.addButtonPressedHandler(adjustSpeedDown, decreaseSpeed)
    gamepad.addButtonPressedHandler(changeColourUp, increaseColours)
    gamepad.addButtonPressedHandler(changeColourDown, decreaseColours)
    gamepad.addButtonPressedHandler(playSound1, sound1ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound2, sound2ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound3, sound3ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound4, sound4ButtonPressed)
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
                servo.servoMovement(-10, 0)
                print('Camera UP ') 
            
            elif gamepad.axis(cameraVertical) == 1:
                servo.servoMovement(10, 0)
                print('Camera Down ')
            
            elif gamepad.axis(cameraHorizontal) == -1:
                servo.servoMovement(0, 10)
                print('Camera Left ')
                
            elif gamepad.axis(cameraHorizontal) == 1:
                servo.servoMovement(0, -10)
                print('Camera Right ')
        
            else:
                alphaBot2.stop();
        
            time.sleep(pollInterval)
        
    except Exception as e:
            print e.message
    finally:
    # Ensure the background thread is always terminated when we are done
        gamepad.disconnect()


