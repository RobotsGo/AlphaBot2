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
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#Set center camera pos
centreHorizontal = 90
centreVertical = 90

global hAngel
global vAngel
hAngel = 0
vAngel = 0

def centreServos():
    kit.servo[0].angle = centreHorizontal
    kit.servo[1].angle = centreVertical
    hAngel = int(kit.servo[0].angle)
    vAngel = int(kit.servo[1].angle)

def horizontalLeft():
    hAngel = int(kit.servo[0].angle)

    if hAngel < 175:  
        kit.servo[0].angle = (int(hAngel) + 2)

    hAngel = int(kit.servo[0].angle)

def horizontalRight():
    hAngel = int(kit.servo[0].angle)
    
    if hAngel > 5:
        kit.servo[0].angle = (int(hAngel) - 2)

    hAngel = int(kit.servo[0].angle)

def verticalUp():
    vAngel = int(kit.servo[1].angle)
    
    if vAngel > 5:
        kit.servo[1].angle = (int(vAngel) - 2)

    vAngel = int(kit.servo[1].angle)
    
def verticalDown():
    vAngel = int(kit.servo[1].angle)
    
    if vAngel < 175:
        kit.servo[1].angle = (int(vAngel) + 2)
    
    vAngel = int(kit.servo[1].angle)
