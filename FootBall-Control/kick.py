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

import RPi.GPIO as GPIO
import time

TRIG = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)



def kickBall():
	try:
		print("kick")
		GPIO.output(TRIG,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(TRIG,GPIO.LOW)
	except Exception as e:
           print e.message
	
def kickClear():
	GPIO.cleanup()
	print("GPIO Cleanup")
