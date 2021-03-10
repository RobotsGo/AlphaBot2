#!/usr/bin/env python
#coding: utf-8

import sys
sys.path.insert(0, "/home/pi/AlphaBot2/python")
from PCA9685 import PCA9685

try:
	pwm = PCA9685(0x40)
	pwm.setPWMFreq(50)
	
	    #Set the Horizontal servo parameters
	horizontalPulse = 1500  #Sets the initial Pulse
	horizontalStep = 0      #Sets the initial step length
	
	    #Set the vertical servo parameters
	verticalPulse = 1500  #Sets the initial Pulse
	verticalStep = 0      #Sets the initial step length
	
	pwm.setServoPulse(1,verticalPulse)
	pwm.setServoPulse(0,horizontalPulse)

except Exception as e:
       print(e.message)
	

def servoMovement(vStep, hStep):
	try:
		horizontalStep = hStep
		verticalStep = vStep
	
		global horizontalPulse,verticalPulse,horizontalStep,verticalStep,pwm
			
		if(horizontalStep != 0):
			horizontalPulse += horizontalStep
			if(horizontalPulse >= 2500): 
				horizontalPulse = 2500
			if(horizontalPulse <= 500):
				horizontalPulse = 500
			pwm.setServoPulse(0,horizontalPulse)    
			
		if(verticalStep != 0):
			verticalPulse += verticalStep
			if(verticalPulse >= 2500): 
				verticalPulse = 2500
			if(verticalPulse <= 500):
				verticalPulse = 500
			pwm.setServoPulse(1,verticalPulse)
	
	except Exception as e:
			print(e.message)
			
def servoClear():
	pwm.write(0x00, 0x20)
	pwm.write(0x00, 0x01)
	pwm.write(0x01, 0x04)
