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
from AlphaBot2 import AlphaBot2

global running
running = True

def exitButtonPressed():
    global running
    running = False
    

def kickButtonPressed():
    print("Nothing yet")

def steamMappingStart():
    
    alphaBot2 = AlphaBot2()
    
    MEDIUM_SPEED_PWMA =  70
    MEDIUM_SPEED_PWMB =  70
    alphaBot2.setPWMA(MEDIUM_SPEED_PWMA);
    alphaBot2.setPWMB(MEDIUM_SPEED_PWMB);

    gamepadType = Gamepad.Steam
    buttonExit = 'HOME'
    buttonKick = 'A'
    triggerForwards = 'RTA'
    triggerBackwards = 'LTA'
    steering = 'AS -X'
    pollInterval = 0.1

    if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)
    gamepad = gamepadType()
    print('Gamepad connected, setup complete') 

# Start the background updating
    gamepad.startBackgroundUpdates()
    
    gamepad.addButtonPressedHandler(buttonKick, kickButtonPressed)
    gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)

# Joystick events handled in the background
    try:
        while running and gamepad.isConnected():
            
            if gamepad.axis(steering) == 1:
                print('Right') 
                alphaBot2.right();
            
            elif gamepad.axis(steering) == -1:
                print('Left')
                alphaBot2.left();
                
            elif gamepad.axis(triggerForwards) == 1:
                print('Forwards')
                alphaBot2.forward();
            
            elif gamepad.axis(triggerBackwards) == 1:
                print('Backwards')
                alphaBot2.backward();
        
            else:
                alphaBot2.stop();
        
            time.sleep(pollInterval)
        
    except Exception as e:
            print e.message
    finally:
    # Ensure the background thread is always terminated when we are done
        gamepad.disconnect()


 
