#!/usr/bin/env python
#coding: utf-8
 
import sys, os
sys.path.insert(0, "/home/pi/Gamepad")
sys.path.insert(1, "/home/pi/AlphaBot2/python")

import Gamepad
import time
import led
import speed
import servo
#import audio
from AlphaBot2 import AlphaBot2

global running
running = True

def sound1ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundOne()

def sound2ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundTwo()

def sound3ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundThree()

def sound4ButtonPressed():
    print("On board Audio and rpi_ws281x both use the same PWM Cannot be used at the same time\n" +
    "https://github.com/jgarff/rpi_ws281x for details")
    #audio.soundFour()

def setSpeed():
    
    if (SPEED_MODE == 1):
        alphaBot2.setPWMA(speed.LOW_SPEED_PWMA);
        alphaBot2.setPWMB(speed.LOW_SPEED_PWMB);

    elif(SPEED_MODE == 2):
        alphaBot2.setPWMA(speed.MEDIUM_SPEED_PWMA);
        alphaBot2.setPWMB(speed.MEDIUM_SPEED_PWMB);
        
    elif(SPEED_MODE == 3):
        alphaBot2.setPWMA(speed.HIGH_SPEED_PWMA);
        alphaBot2.setPWMB(speed.HIGH_SPEED_PWMB);
        
    else:
        alphaBot2.setPWMA(speed.LOW_SPEED_PWMA);
        alphaBot2.setPWMB(speed.LOW_SPEED_PWMB);

def exitButtonPressed():
    global running
    running = False

def steamMappingStart():
    
    global SPEED_MODE
    SPEED_MODE = 1
    
    global SELECTED_COLOUR
    SELECTED_COLOUR = 0
    
    COLOURS =  ['off', 'Red', 'Green', 'Blue', 'White']
    
    global alphaBot2
    alphaBot2 = AlphaBot2()
    
    gamepadType = Gamepad.Steam
    buttonExit = 'HOME'
    triggerForwards = 'RTA'
    triggerBackwards = 'LTA'
    steering = 'AS -X'
    cameraVertical = 'LTP -Y'
    cameraHorizontal = 'LTP -X'
    adjustSpeed = 'RTP -Y'
    changeColour = 'LTP -Y'
    playSound1 = 'A'
    playSound2 = 'B'
    playSound3 = 'X'
    playSound4 = 'Y'
    pollInterval = 0.1

    if not Gamepad.available():
        print('Please connect your gamepad...')
        while not Gamepad.available():
            time.sleep(1.0)
    gamepad = gamepadType()
    print('Gamepad connected, setup complete') 

# Start the background updating
    gamepad.startBackgroundUpdates()
    gamepad.addButtonPressedHandler(playSound1, sound1ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound2, sound2ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound3, sound3ButtonPressed)
    gamepad.addButtonReleasedHandler(playSound4, sound4ButtonPressed)
    gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)

# Joystick events handled in the background
    try:
        while running and gamepad.isConnected():
        
            if gamepad.axis(triggerBackwards) == 1:
                print('Backwards')
                alphaBot2.backward();
            
            elif gamepad.axis(triggerForwards) == 1:
                print('Forwards')
                alphaBot2.forward();
            
            elif gamepad.axis(steering) == 1:
                print('Right') 
                alphaBot2.right();
            
            elif gamepad.axis(steering) == -1:
                print('Left')
                alphaBot2.left();
            
            elif gamepad.axis(cameraVertical) < 0:
                servo.servoMovement(-10, 0)
                print('Camera UP ') 
            
            elif gamepad.axis(cameraVertical) > 0:
                servo.servoMovement(10, 0)
                print('Camera Down ')
            
            elif gamepad.axis(cameraHorizontal) < 0:
                servo.servoMovement(0, 10)
                print('Camera Left ')
                
            elif gamepad.axis(cameraHorizontal) > 0:
                servo.servoMovement(0, -10)
                print('Camera Right ')
        
            elif gamepad.axis(adjustSpeed) < 0:
                if SPEED_MODE < 3:
                    SPEED_MODE = (SPEED_MODE + 1) 
                    setSpeed()
                    print('Speed mode ' + str(SPEED_MODE)) 
            
                else:
                    print('Speed mode ' + str(SPEED_MODE))
                
            elif gamepad.axis(adjustSpeed) > 0:
                if SPEED_MODE > 1:
                    SPEED_MODE = (SPEED_MODE - 1)
                    setSpeed() 
                    print('Speed mode ' + str(SPEED_MODE))
            
                else:
                    print('Speed mode ' + str(SPEED_MODE))  
                
            elif gamepad.axis(changeColour) > 0:
                if  SELECTED_COLOUR < 4:
                    SELECTED_COLOUR = (SELECTED_COLOUR + 1)
                    led.setColour(SELECTED_COLOUR)
                    print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR)) 
            
                else:
                    print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
            
            elif gamepad.axis(changeColour) < 0:
                if SELECTED_COLOUR > 0:
                    SELECTED_COLOUR = (SELECTED_COLOUR - 1)
                    led.setColour(SELECTED_COLOUR) 
                    print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))
            
                else:
                    print('Change colour to: ' + str(COLOURS[SELECTED_COLOUR]) + ' ' + str(SELECTED_COLOUR))  
        
            else:
                alphaBot2.stop();
        
            time.sleep(pollInterval)
        
    except Exception as e:
            print e.message
    finally:
    # Ensure the background thread is always terminated when we are done
        gamepad.disconnect()


