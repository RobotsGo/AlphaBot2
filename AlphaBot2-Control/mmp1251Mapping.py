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

import sys
import os
import Gamepad
import time
import led
import servo
import kick
import motors as motor
import socket
import buzzer
import netifaces
 
RUNNING = True
SPEED_MODE = 1 
SELECTED_COLOUR = 0  
COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']

def buzzerSoundOff():
    buzzer.buzzOff()

def buzzerSound():
    buzzer.buzzOn()

def centreServo():
    servo.centreServos()

def kickButtonPressed():
    kick.kickBall()
    
def selectSpeed(num):
    if num < 0:
	    increaseSpeed()
    
    if num > 0:
	    decreaseSpeed()

def selectColour(num):
    if num > 0:
	    increaseColours()
    
    if num < 0:
	    decreaseColours()
    
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

def setSpeed():
    #Speed tuning motor.Speed(MOTOR1, MOTOR2)
    #Looking from the front (USB PORTS) MOTOR1 is on your right
    #Increase the slower wheel 0.1 till bot moves stright ish. 
    if (SPEED_MODE == 1):
        motor.Speed(0.3, 0.2) #default (0.2, 0.2)

    elif(SPEED_MODE == 2):
        motor.Speed(0.6, 0.5) #default (0.5, 0.5)
        
    elif(SPEED_MODE == 3):
        motor.Speed(0.9, 0.8) #default (0.5, 0.5)
    
    else:
        motor.Speed(0.3, 0.2) #default (0.2, 0.2)
        
def exitButtonPressed():
    led.clearLed()
    centreServo()
    global RUNNING
    RUNNING = False
    sys.exit()

def MMP1251Start():
    global SPEED_MODE
    SPEED_MODE = 1
    
    global SELECTED_COLOUR
    SELECTED_COLOUR = 0
    
    COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']
    
    centreServo()
    
    GAME_PAD_TYPE = Gamepad.MMP1251
    BUTTON_EXIT = 'HOME'
    TRIGGER_FORWARDS = 'R2'
    TRIGGER_BACKWARDS = 'L2'
    STEERING = 'RIGHT-X'
    CAMERA_VERTICAL = 'LEFT-Y'
    CAMERA_HORIZONTAL = 'LEFT-X'
    ADJUST_SPEED = 'DPAD-Y'
    CHANGE_COLOUR = 'DPAD-X'
    BUTTON_KICK = 'A'
    BUTTON_CENTRE_SERVOS = 'Y'
    BUTTON_BUZZER = 'X'
    POLL_INTERVAL = 0.1
    
    INT_FACE = netifaces.ifaddresses('wlan0')
    HOST_IP = INT_FACE[netifaces.AF_INET][0]['addr']
    
    print("AlphBot2 streaming and MMP1251 Mod My Pi control server version 0.1")
    print("RobotsGo web https://robotsgo.net/")
    print("RobotsGo webhttps://github.com/RobotsGo")
    print("")
    
    if HOST_IP != " ":
        print("Video Stream will be available @ http://" + str(HOST_IP) + ":8000")
        print("To use VLC etc, Video Stream will be available @ http://" + str(HOST_IP) + ":8000/stream")
    
    if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)
    gamepad = GAME_PAD_TYPE()
    
    #Buzz buzz when controller is connected.
    buzzerSound()
    time.sleep(0.1)
    buzzerSoundOff()
    time.sleep(0.1)
    buzzerSound()
    time.sleep(0.1)
    buzzerSoundOff()
    
    print('Gamepad connected, setup complete') 
    
    # Start the background updating
    gamepad.startBackgroundUpdates()
    gamepad.addButtonPressedHandler(BUTTON_KICK, kickButtonPressed)
    gamepad.addButtonPressedHandler(BUTTON_EXIT, exitButtonPressed)
    gamepad.addButtonPressedHandler(BUTTON_CENTRE_SERVOS, centreServo)
    gamepad.addButtonPressedHandler(BUTTON_BUZZER, buzzerSound)
    gamepad.addButtonReleasedHandler(BUTTON_BUZZER, buzzerSoundOff)
    gamepad.addAxisMovedHandler(ADJUST_SPEED, selectSpeed)
    gamepad.addAxisMovedHandler(CHANGE_COLOUR, selectColour)
    
    # Joystick events handled in the background
    try:
        while RUNNING and gamepad.isConnected():
        
            if gamepad.axis(TRIGGER_BACKWARDS) == 1:
                print('Backwards')
                motor.backwards()

            elif gamepad.axis(TRIGGER_FORWARDS) == 1:
                print('Forwards')
                motor.forwards()
            
            elif gamepad.axis(STEERING) == 1:
                print('Right')
                motor.right()

            elif gamepad.axis(STEERING) == -1:
                print('Left')
                motor.left()
            
            elif gamepad.axis(CAMERA_VERTICAL) == -1:
                servo.verticalUp()
                print('Camera UP ') 
            
            elif gamepad.axis(CAMERA_VERTICAL) == 1:
                servo.verticalDown()
                print('Camera Down ')
            
            elif gamepad.axis(CAMERA_HORIZONTAL) == -1:
                servo.horizontalLeft()
                print('Camera Left ')
                
            elif gamepad.axis(CAMERA_HORIZONTAL) == 1:
                servo.horizontalRight()
                print('Camera Right ')
        
            else:
                motor.stopMotor();
        
        time.sleep(POLL_INTERVAL)
        
    except Exception as e:
            print(e.message)
    finally:
    # Ensure the background thread is always terminated when we are done
        gamepad.disconnect()

MMP1251Start()
