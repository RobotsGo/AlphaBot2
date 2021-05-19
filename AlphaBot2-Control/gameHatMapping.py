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

host = " "
port = 5000
connected = False
receivedBuffer = ""
sendBuffer = ""

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="Connect to server ip address --server 192.168.1.1", type=str)
args = parser.parse_args()

if(args.server != ""):
    host = args.server

def appQuit():
    #listener.stop()
    sendBuff = "shutdown"
    client_socket.send(sendBuff.encode())
    connected = False
    client_socket.close()
    sys.exit()

def halt():
    sendBuff = "halt"
    client_socket.send(sendBuff.encode())

def speedMode():
    sendBuff = "2"
    client_socket.send(sendBuff.encode())

def moveForwards():
    sendBuff = "up"
    client_socket.send(sendBuff.encode())

def moveBackwards():
    sendBuff = "down"
    client_socket.send(sendBuff.encode())  
    
def moveLeft():
    sendBuff = "left"
    client_socket.send(sendBuff.encode())

def moveRight():
    sendBuff = "right"
    client_socket.send(sendBuff.encode())

def kick():
    sendBuff = "space"
    client_socket.send(sendBuff.encode())

def centreServo():
    sendBuff = "q"
    client_socket.send(sendBuff.encode())
    
def cameraVertical(num):
    if num < 0:
        sendBuff = "w"
        client_socket.send(sendBuff.encode())
    
    if num > 0:
        sendBuff = "s"
        client_socket.send(sendBuff.encode())
    
def cameraHorizontal(num):
    if num > 0:
        sendBuff = "a"
        client_socket.send(sendBuff.encode())
    
    if num < 0:
        sendBuff = "d"
        client_socket.send(sendBuff.encode())
        
try:        
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    connected = True
except Exception as e:
        print(e.message)

speedMode()

GAME_PAD_TYPE = Gamepad.GameHat
BUTTON_EXIT = 'START'
FORWARDS = 'X'
BACKWARDS = 'B'
STEERING_LEFT = 'Y'
STEERING_RIGHT = 'A'
CAMERA_VERTICAL = 'LEFT-Y'
CAMERA_HORIZONTAL = 'LEFT-X'
CAMERA_CENTER = 'TL'
BUTTON_KICK = 'TR'
BUTTON_CENTRE_SERVOS = 'SELECT'
POLL_INTERVAL = 0.1

if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)

gamepad = GAME_PAD_TYPE()

gamepad.startBackgroundUpdates()
gamepad.addButtonPressedHandler(BUTTON_EXIT, appQuit)
gamepad.addButtonPressedHandler(FORWARDS, moveForwards)
gamepad.addButtonReleasedHandler(FORWARDS, halt)
gamepad.addButtonPressedHandler(BACKWARDS, moveBackwards)
gamepad.addButtonReleasedHandler(BACKWARDS, halt)
gamepad.addButtonPressedHandler(STEERING_LEFT, moveLeft)
gamepad.addButtonReleasedHandler(STEERING_LEFT, halt)
gamepad.addButtonPressedHandler(STEERING_RIGHT, moveRight)
gamepad.addButtonReleasedHandler(STEERING_RIGHT, halt)
gamepad.addButtonPressedHandler(BUTTON_KICK, kick)
gamepad.addButtonReleasedHandler(BUTTON_KICK, halt)
gamepad.addButtonPressedHandler(BUTTON_CENTRE_SERVOS, centreServo)
gamepad.addButtonReleasedHandler(BUTTON_CENTRE_SERVOS, halt)
gamepad.addAxisMovedHandler(CAMERA_VERTICAL, cameraVertical)
gamepad.addAxisMovedHandler(CAMERA_HORIZONTAL, cameraHorizontal)

print("AlphBot2 WaveShare rpi GameHat control client version 0.1")
print("RobotsGo web https://robotsgo.net/")
print("RobotsGo webhttps://github.com/RobotsGo")
print("")
print("Video Stream will be available @ http://" + str(host) + ":8000")
print("To use VLC etc, Video Stream will be available @ http://" + str(host) + ":8000/stream")

while connected == True:
    receivedBuffer = client_socket.recv(1024).decode()
    print("From " + host + ":" + str(receivedBuffer))
    
appQuit()
