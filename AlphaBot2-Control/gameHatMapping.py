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

import threading
import time
import argparse
import socket
import sys
import Gamepad

#import sys
#import os
#import Gamepad
#import time
#import led
#import servo
#import kick
#import motors as motor
#import socket
#import buzzer
 
RUNNING = True
SPEED_MODE = 2 

SERVER_IP = " "
PORT = 5000
connected = False
receivedBuffer = ""
sendBuffer = ""

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="Connect to server ip address --server 192.168.1.1", type=str)
args = parser.parse_args()

if(args.server != ""):
    SERVER_IP = args.server
    
def appQuit():
    RUNNING = False
    connected = False
    client_socket.close()
    sys.exit()

def centreServo():
    sendBuff = "q"
    client_socket.send(sendBuff.encode())

def kickButtonPressed():
    sendBuff = "space"
    client_socket.send(sendBuff.encode())

#def setSpeed():
    
    #if (SPEED_MODE == 1):
	    #motor.Speed(0.2, 0.2)

    #elif(SPEED_MODE == 2):
	    #motor.Speed(0.5, 0.5)
        
    #elif(SPEED_MODE == 3):
	    #motor.Speed(0.8, 0.8)
    
    #else:
	    #motor.Speed(0.2, 0.2)
        
def exitButtonPressed():
    global RUNNING
    RUNNING = False
    sys.exit()

def gameHatStart():
    
    GAME_PAD_TYPE = Gamepad.GameHat
    BUTTON_EXIT = 'START'
    BUTTON_FORWARDS = 'X'
    BUTTON_BACKWARDS = 'B'
    STEERING_LEFT = 'Y'
    STEERING_RIGHT = 'A'
    CAMERA_VERTICAL = 'LEFT-Y'
    CAMERA_HORIZONTAL = 'LEFT-X'
    BUTTON_KICK = 'TR'
    BUTTON_CENTRE_SERVOS = 'SELECT'
    BUTTON_BUZZER = 'TL'
    POLL_INTERVAL = 0.1
    
    try:
        global client_socket
        client_socket = socket.socket()  # instantiate
        client_socket.connect((SERVER_IP, PORT))  # connect to the server
        connected = True

    except Exception as e:
	    print(e)
    
    print("AlphBot2 streaming and WaveShare GameHat control server version 0.1")
    print("RobotsGo web https://robotsgo.net/")
    print("RobotsGo webhttps://github.com/RobotsGo")
    print("")
    print("Video Stream will be available @ http://" + str(SERVER_IP) + ":8000")
    print("To use VLC etc, Video Stream will be available @ http://" + str(SERVER_IP) + ":8000/video_feed")
    
    if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)
    gamepad = GAME_PAD_TYPE()
    
    #Buzz buzz when controller is connected.
    #buzzerSound()
    #time.sleep(0.1)
    #buzzerSoundOff()
    #time.sleep(0.1)
    #buzzerSound()
    #time.sleep(0.1)
    #buzzerSoundOff()
    
    print('Gamepad connected, setup complete') 
    
    # Start the background updating
    gamepad.startBackgroundUpdates()
    #gamepad.addButtonPressedHandler(ADJUST_SPEED_UP, increaseSpeed)
    #gamepad.addButtonPressedHandler(ADJUST_SPEED_DOWN, decreaseSpeed)
    #gamepad.addButtonPressedHandler(CHANGE_COLOUR_UP, increaseColours)
    #gamepad.addButtonPressedHandler(CHANGE_COLOUR_DOWN, decreaseColours)
    gamepad.addButtonPressedHandler(BUTTON_KICK, kickButtonPressed)
    gamepad.addButtonPressedHandler(BUTTON_EXIT, exitButtonPressed)
    gamepad.addButtonPressedHandler(BUTTON_CENTRE_SERVOS, centreServo)
    #gamepad.addButtonPressedHandler(BUTTON_BUZZER, buzzerSound)
    #gamepad.addButtonReleasedHandler(BUTTON_BUZZER, buzzerSoundOff)
    
    # Joystick events handled in the background
    try:
	    while RUNNING and gamepad.isConnected():
		    
		    if gamepad.axis(CAMERA_VERTICAL) == -1:
			    sendBuff = "w"
                client_socket.send(sendBuff.encode()) 
            
		    elif gamepad.axis(CAMERA_VERTICAL) == 1:
			    sendBuff = "s"
                client_socket.send(sendBuff.encode())
            
		    elif gamepad.axis(CAMERA_HORIZONTAL) == -1:
			    sendBuff = "d"
                client_socket.send(sendBuff.encode())
                
		    elif gamepad.axis(CAMERA_HORIZONTAL) == 1:
			    sendBuff = "a"
                client_socket.send(sendBuff.encode())
        
		    else:
			    sendBuff = "halt"
                client_socket.send(sendBuff.encode())
        
	    time.sleep(POLL_INTERVAL)
        
    except Exception as e:
            print(e.message)
    finally:
    # Ensure the background thread is always terminated when we are done
        gamepad.disconnect()

ps3MappingStart()
 
