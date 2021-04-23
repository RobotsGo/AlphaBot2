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

import time
import sys
import socket
import led
import servo
import kick
import buzzer
import motors as motor
import netifaces 

HOST_IP = ""
HOST_PORT = 5000
RECEIVE_BUFF = ""
SEND_BUFF = ""
SPEED_MODE = 1 
SELECTED_COLOUR = 0  
COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']


def buzzerSoundOff():
    buzzer.buzzOff()

def buzzerSound():
    buzzer.buzzOn()

#Cycle through LED colours 'led.py'	
def increaseColours():
    global SELECTED_COLOUR
    global COLOURS
    if SELECTED_COLOUR < 4:
        SELECTED_COLOUR = (SELECTED_COLOUR + 1)
        led.setColour(SELECTED_COLOUR)
        print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR)) 
            
    else:
        print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))

#Cycle through LED colours 'led.py'
def decreaseColours():
    global SELECTED_COLOUR
    global COLOURS
    if SELECTED_COLOUR > 0:
        SELECTED_COLOUR = (SELECTED_COLOUR - 1)
        led.setColour(SELECTED_COLOUR) 
        print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
    else:
        print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))

#Set speed mode 
def setSpeed():
    
    if (SPEED_MODE == 1):
        motor.Speed(0.2, 0.2)

    elif(SPEED_MODE == 2):
        motor.Speed(0.5, 0.5)
        
    elif(SPEED_MODE == 3):
        motor.Speed(0.8, 0.8)
    
    else:
        motor.Speed(0.2, 0.2)

def networkMappingStart():
    servo.centreServos()
#Get real server ip address not localhost
    
    global SPEED_MODE
    
    INT_FACE = netifaces.ifaddresses('wlan0')
    HOST_IP = INT_FACE[netifaces.AF_INET][0]['addr']
    
    print("AlphBot2 streaming and network server version 0.1")
    print("RobotsGo web https://robotsgo.net/")
    print("RobotsGo webhttps://github.com/RobotsGo")
    print("")
    
    if HOST_IP != " ":
        print("Video Stream will be available @ http://" + str(HOST_IP) + ":8000")
        print("To use VLC etc, Video Stream will be available @ http://" + str(HOST_IP) + ":8000/video_feed")	 
    print("Starting network control server....")
    
    #Get socket instance
    server_socket = socket.socket()  
    
    #Look closely. The bind() function takes tuple as argument
    #Bind host address and port together
    server_socket.bind((HOST_IP, HOST_PORT)) 
    
    print("Server reachable @ " + HOST_IP + ":" + str(HOST_PORT) )
    
    #Configure how many client the server can listen simultaneously
    server_socket.listen(1)
    
    #Accept new connection
    conn, address = server_socket.accept()
    
    #Print ip of client when connected 
    print("Connection from: " + str(address))
    
    #Set Connected so while loops will start.
    connected = True
    
    #Buzz buzz when client is connected.
    
    buzzerSound()
    time.sleep(0.1)
    buzzerSoundOff()
    time.sleep(0.1)
    buzzerSound()
    time.sleep(0.1)
    buzzerSoundOff()
    
    
    
    #Main function loop, match receiveBuff data with functions in 'kick.py, alphaBot.py, servo.py and led.py
    while True:
    
    # receive data stream. it won't accept data packet greater than 1024 bytes

        RECEIVE_BUFF = conn.recv(1024).decode()
    
        if RECEIVE_BUFF == "shutdown":
            print("shutdown received")
            connected = False
            servo.centreServos()
            led.clearLed()
            conn.close()
            motor.stopMotor()
            sys.exit()

        elif RECEIVE_BUFF == "space":
            print("space received")
            SEND_BUFF = "kick"
            kick.kickBall()
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "left":
            print("left key received")
            motor.left()
            SEND_BUFF = "Left"
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "right":
            print("right key received")
            motor.right()
            SEND_BUFF = "Right"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "up":
            print("up key received")
            motor.forwards()
            SEND_BUFF = "Forward"
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "down":
            print("down key received")
            motor.backwards()
            SEND_BUFF = "Backwards"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "w":
            print("w key received")
            servo.verticalUp()
            SEND_BUFF = "Camera UP"
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "s":
            print("s key received")
            servo.verticalDown()
            SEND_BUFF = "Camera Down "
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "a":
            print("a key received")
            servo.horizontalLeft()
            SEND_BUFF = "Camera Left"
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "d":
            print("d key received")
            servo.horizontalRight()
            SEND_BUFF = "Camera Right"
            conn.send(SEND_BUFF.encode())
        
        elif RECEIVE_BUFF == "1":
            print("1 key received")
            SPEED_MODE = 1
            setSpeed()
            SEND_BUFF = "Speed mode set to LOW"
            conn.send(SEND_BUFF.encode())
            
        elif RECEIVE_BUFF == "2":
            print("2 key received")
            SPEED_MODE = 2
            setSpeed()
            SEND_BUFF = "Speed mode set to Medium"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "3":
            print("3 key received")
            SPEED_MODE = 3
            setSpeed()
            SEND_BUFF = "Speed mode set to High"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == ".":
            print("Increase Colours")
            increaseColours()
            SEND_BUFF = "Increase Colours"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == ",":
            print("Decrease Colours")
            decreaseColours()
            SEND_BUFF = "Decrease Colours"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "q":
            print("Centre Camera")
            servo.centreServos()
            SEND_BUFF = "Centre Camera"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "e":
            print("Buzz")
            buzzerSound()
            time.sleep(0.1)
            buzzerSoundOff()
            SEND_BUFF = "Buzz"
            conn.send(SEND_BUFF.encode())

        elif RECEIVE_BUFF == "halt":
            motor.stopMotor()

        else:
            motor.stopMotor()


networkMappingStart()