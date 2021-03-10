#!/usr/bin/env python
#coding: utf-8

import os
import sys
import RPi.GPIO as GPIO
sys.path.insert(0, "/home/pi/AlphaBot2/python")


import version
import camera
import led
import servo
import argparse
import xboxOneMapping
import steamMapping

def exitApp():
    print("Clear LED's")
    led.clear()
    print("DONE..")
    
    print("Clear all GPIO's")
    GPIO.cleanup()
    print("Done..")
    
    print("Clear Servos")
    servo.servoClear()
    print("Done..")
    
    print("App Exiting")
    sys.exit()


if not (os.getuid() == 0):
    sys.exit('Script needs to be run as root, eg $ sudo python main.py -g Steam')

GAME_PAD_SELECTED = int(0)

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--camera", help="Disable mpeg streamer", action='store_true')
parser.add_argument("-g", "--gamepad", help="GamePad you would like to use to control the robot. Options are XboxOne or Steam", type=str)
parser.add_argument("-v", "--version", help="See version and build information", action='store_true')
    
# Read arguments from command line
args = parser.parse_args()
 
if(args.camera):
    
    print("Disable mpeg streamer and servos will not be setup for use")
    camera.cameraOff()

if(args.gamepad):
    
    if(args.gamepad == 'XboxOne'):
        GAME_PAD_SELECTED = int(1)
        print("GamePad in use will be: XboxOne Controller")
        
    elif(args.gamepad == 'Steam'):
        GAME_PAD_SELECTED = int(2)
        print("GamePad in use will be: Steam Controller")
    
    else:
        print("Incorrect controller entered, neither XboxOne or Steam")
        sys.exit()

if(args.version):
    version.show()
    sys.exit()

if(GAME_PAD_SELECTED == 0):
    print("No GamePad Selected!!!, Exiting")
    sys.exit()
    
if(GAME_PAD_SELECTED == 1):
    xboxOneMapping.xboxOneMappingStart()
    
if(GAME_PAD_SELECTED == 2):
    steamMapping.steamMappingStart()
    
exitApp()

    

    
