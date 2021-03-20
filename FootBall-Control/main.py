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

import os
import sys
sys.path.insert(0, "/home/pi/AlphaBot2/python")


import version
import camera
import team
import argparse
import kick
import xboxOneMapping
import steamMapping
import ps3Mapping



def exitApp():
    print("App Exiting")
    team.clearTeam()
    kick.kickClear()
    sys.exit()


if not (os.getuid() == 0):
    sys.exit('Script needs to be run as root, eg $ sudo python main.py -g Steam -t blue')

GAME_PAD_SELECTED = int(0)
TEAM_SELECTED = int(0)

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--camera", help="Disable mpeg streamer", action='store_true')
parser.add_argument("-g", "--gamepad", help="GamePad you would like to use to control the robot. Options are XboxOne, Steam or PS3", type=str)
parser.add_argument("-t", "--team", help="Set the Robot's team colour. Options are blue or red.", type=str)
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
        
    elif(args.gamepad == 'PS3'):
        GAME_PAD_SELECTED = int(3)
        print("GamePad in use will be: Steam Controller")
    
        
    else:
        print("Incorrect controller entered, either XboxOne or Steam")
        sys.exit()

if(args.team):
    
    if(args.team == 'red'):
        TEAM_SELECTED = int(1)
        print("AlphaBot joining the RED TEAM")
        
    elif(args.team == 'blue'):
        TEAM_SELECTED = int(2)
        print("AlphaBot joining the BLUE TEAM")
    
    else:
        print("No team colour entered either red or blue")
        sys.exit()

if(args.version):
    version.show()
    sys.exit()

if(GAME_PAD_SELECTED == 0 and TEAM_SELECTED == 0):
    print("No application arguments given!!!")
    exitApp()
    
if(GAME_PAD_SELECTED == 1):
    team.setTeam(int(TEAM_SELECTED))
    xboxOneMapping.xboxOneMappingStart()
    
if(GAME_PAD_SELECTED == 2):
    team.setTeam(int(TEAM_SELECTED))
    steamMapping.steamMappingStart()
    
if(GAME_PAD_SELECTED == 3):
    team.setTeam(int(TEAM_SELECTED))
    ps3Mapping.ps3MappingStart()

    
exitApp()

    

    
