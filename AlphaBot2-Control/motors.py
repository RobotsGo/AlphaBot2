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

from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

# GPIO 6 is used for Generating Software PWM
# GPIO 12 & GPIO 13  are used for Motor control pins as per schematic 
PWM_PIN_MOT1 = 6
IN1_PIN_MOT1 = 12
IN2_PIN_MOT1 = 13

# GPIO 26 is used for Generating Software PWM
# GPIO 20 & GPIO 21  are used for Motor control pins as per schematic 
PWM_PIN_MOT2 = 26
IN1_PIN_MOT2 = 20
IN2_PIN_MOT2 = 21
	
	
	# PWMOutputDevice takes  BCM_PIN number
	# Active High 
	# intial value
	# PWM Frequency
	# and Pin_factory which can be ignored
	
pwm_pin_mot1 = PWMOutputDevice (PWM_PIN_MOT1,True, 0, 1200)
pwm_pin_mot2 = PWMOutputDevice (PWM_PIN_MOT2,True, 0, 1200)
	
	# DigitalOutputDevice take 
	# Pin Nuumber
	# Active High
	#Initial Value
	
cw_pin_mot1 = DigitalOutputDevice (IN1_PIN_MOT1, True, 0)
ccw_pin_mot1 = DigitalOutputDevice (IN2_PIN_MOT1, True, 0)
	
cw_pin_mot2 = DigitalOutputDevice (IN1_PIN_MOT2, True, 0)
ccw_pin_mot2 = DigitalOutputDevice (IN2_PIN_MOT2, True, 0)
	
	# Set Speed default to low	
SPEED_MOT1 = 0.2
SPEED_MOT2 = 0.2
	
def Speed(MOT1, MOT2):
	
	global SPEED_MOT1
	global SPEED_MOT2	
	SPEED_MOT1 = MOT1
	SPEED_MOT2 = MOT2

def stopMotor():
	
	cw_pin_mot1.value = 0
	ccw_pin_mot1.value = 0
	pwm_pin_mot1.value = 0
	
	cw_pin_mot2.value = 0
	ccw_pin_mot2.value = 0
	pwm_pin_mot2.value = 0
	        
	        
def forwards():
		
	pwm_percnt1 = SPEED_MOT1
	pwm_pin_mot1.value = pwm_percnt1
	cw_pin_mot1.value = 0
	ccw_pin_mot1.value = 1
		
	pwm_percnt2 = SPEED_MOT2
	pwm_pin_mot2.value = pwm_percnt2
	cw_pin_mot2.value = 0
	ccw_pin_mot2.value = 1
		
def backwards():
		
	pwm_percnt1 = SPEED_MOT1
	pwm_pin_mot1.value = pwm_percnt1
	cw_pin_mot1.value = 1
	ccw_pin_mot1.value = 0
		
	pwm_percnt2 = SPEED_MOT2
	pwm_pin_mot2.value = pwm_percnt2
	cw_pin_mot2.value = 1
	ccw_pin_mot2.value = 0
		
def left():
	
	pwm_percnt1 = SPEED_MOT1
	pwm_pin_mot1.value = pwm_percnt1
	cw_pin_mot1.value = 1
	ccw_pin_mot1.value = 0
		
	pwm_percnt2 = SPEED_MOT2 
	pwm_pin_mot2.value = pwm_percnt2
	cw_pin_mot2.value = 0
	ccw_pin_mot2.value = 1
	
def right():
	
	pwm_percnt1 = SPEED_MOT1
	pwm_pin_mot1.value = pwm_percnt1
	cw_pin_mot1.value = 0
	ccw_pin_mot1.value = 1
		
	pwm_percnt2 = SPEED_MOT2 
	pwm_pin_mot2.value = pwm_percnt2
	cw_pin_mot2.value = 1
	ccw_pin_mot2.value = 0
