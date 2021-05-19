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
from pynput import keyboard

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
    listener.stop()
    client_socket.close()
    sys.exit()
        
def on_press(key):
    if(key == keyboard.Key.esc):
        sendBuff = "shutdown"
        client_socket.send(sendBuff.encode())
        connected = False
        appQuit()
    
    elif(key == keyboard.Key.space):
        sendBuff = "space"
        client_socket.send(sendBuff.encode())
    
    elif(key == keyboard.Key.left):
        sendBuff = "left"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.right):
        sendBuff = "right"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.up):
        sendBuff = "up"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.down):
        sendBuff = "down"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(119)):
        sendBuff = "w"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(115)):
        sendBuff = "s"
        client_socket.send(sendBuff.encode())
    
    elif(key == keyboard.KeyCode(97)):
        sendBuff = "a"
        client_socket.send(sendBuff.encode())
            
    elif(key == keyboard.KeyCode(100)):
        sendBuff = "d"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(49)):
        sendBuff = "1"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(50)):
        sendBuff = "2"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(51)):
        sendBuff = "3"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(44)):
        sendBuff = ","
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(46)):
        sendBuff = "."
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(113)):
        sendBuff = "q"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.KeyCode(101)):
        sendBuff = "e"
        client_socket.send(sendBuff.encode())
    
    else:
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        print("no recognized input")

def on_release(key):
    
    if(key == keyboard.Key.left):
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.right):
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.up):
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.down):
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        
    elif(key == keyboard.Key.space):
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        
    else:
        sendBuff = "halt"
        client_socket.send(sendBuff.encode())
        print("no recognized input")
        
try:        
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    connected = True
except Exception as e:
        print(e.message)
#Collect events until released
#with keyboard.Listener(on_press=on_press) as listener:listener.join()

#...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
listener.start()

print("AlphBot2 streaming and network control client version 0.1")
print("RobotsGo web https://robotsgo.net/")
print("RobotsGo webhttps://github.com/RobotsGo")
print("")
print("Video Stream will be available @ http://" + str(host) + ":8000")
print("To use VLC etc, Video Stream will be available @ http://" + str(host) + ":8000/stream")

while connected == True:
    receivedBuffer = client_socket.recv(1024).decode()
    print("From " + host + ":" + str(receivedBuffer))
    
appQuit()
