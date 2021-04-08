#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import time
import json
from AlphaBot import AlphaBot
import os
 
LOW_SPEED    =  30
MEDIUM_SPEED =  50
HIGH_SPEED   =  80

os.system("echo \"discoverable on\" | bluetoothctl")
Ab = AlphaBot()
BT = serial.Serial("/dev/rfcomm0",115200)
print('serial test start ...')
BT.flushInput()
 
try:
    while True:
        data = ""
        while BT.inWaiting() > 0:
            data += BT.read(BT.inWaiting())
        if data != "":
            #print data
            try:
                s = json.loads(data)             
                cmd =  s.get("Forward")
                if cmd != None:
                    if cmd == "Down":
                        Ab.forward()
                        BT.write("{\"State\":\"Forward\"}")
                    elif cmd == "Up":
                        BT.write("{\"State\":\"Stop\"}")
                        Ab.stop()
 
                cmd = s.get("Backward")
                if cmd != None:
                    if cmd == "Down":
                        Ab.backward()
                        BT.write("{\"State\":\"Backward\"}")
                    elif cmd == "Up":
                        BT.write("{\"State\":\"Stop\"}")
                        Ab.stop()
                 
                cmd = s.get("Left")
                if cmd != None:
                    if cmd == "Down":
                        Ab.left()
                        BT.write("{\"State\":\"Left\"}")
                    elif cmd == "Up":
                        BT.write("{\"State\":\"Stop\"}")
                        Ab.stop()
                         
                cmd = s.get("Right")
                if cmd != None:
                    if cmd == "Down":
                        Ab.right()
                        BT.write("{\"State\":\"Right\"}")
                    elif cmd == "Up":
                        BT.write("{\"State\":\"Stop\"}")
                        Ab.stop()
                         
                cmd = s.get("Low")
                if cmd == "Down":
                    BT.write("{\"State\":\"Low\"}")
                    Ab.setPWMA(LOW_SPEED);
                    Ab.setPWMB(LOW_SPEED);
 
                cmd = s.get("Medium")
                if cmd == "Down":
                    BT.write("{\"State\":\"Medium\"}")
                    Ab.setPWMA(MEDIUM_SPEED);
                    Ab.setPWMB(MEDIUM_SPEED);
 
                cmd = s.get("High")
                if cmd == "Down":
                    BT.write("{\"State\":\"High\"}")
                    Ab.setPWMA(HIGH_SPEED);
                    Ab.setPWMB(HIGH_SPEED);                 
 
                BT.flushInput()                 
            except ValueError:       #not json format
                continue
except KeyboardInterrupt:
    if BT!= None:
        BT.close()
