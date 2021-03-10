#!/usr/bin/env python
#coding: utf-8

import sys
import RPi.GPIO as GPIO
from rpi_ws281x import Color, PixelStrip, ws

LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP = ws.SK6812_STRIP

try:
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.setBrightness(50)
    strip.begin()

except Exception as e:
        print(e.message)

def setColour(colour):

    try:
        if (colour == 0):
                strip.setPixelColor(0, Color(0, 0, 0, 0)) #None
                strip.setPixelColor(1, Color(0, 0, 0, 0))
                strip.setPixelColor(2, Color(0, 0, 0, 0))
                strip.setPixelColor(3, Color(0, 0, 0, 0))
                strip.show()
                
        elif (colour == 1):
                strip.setPixelColor(0, Color(255, 0, 0)) #Red
                strip.setPixelColor(1, Color(255, 0, 0))
                strip.setPixelColor(2, Color(255, 0, 0))
                strip.setPixelColor(3, Color(255, 0, 0))
                strip.show()
        
        elif (colour == 2):
                strip.setPixelColor(0, Color(0, 255, 0)) #Green
                strip.setPixelColor(1, Color(0, 255, 0))
                strip.setPixelColor(2, Color(0, 255, 0))
                strip.setPixelColor(3, Color(0, 255, 0))
                strip.show()
        
        elif (colour == 3):
                strip.setPixelColor(0, Color(0, 0, 255)) #Blue
                strip.setPixelColor(1, Color(0, 0, 255))
                strip.setPixelColor(2, Color(0, 0, 255))
                strip.setPixelColor(3, Color(0, 0, 255))
                strip.show()
        
        elif (colour == 4):
                strip.setPixelColor(0, Color(255, 255, 255,)) #White
                strip.setPixelColor(1, Color(255, 255, 255,))
                strip.setPixelColor(2, Color(255, 255, 255,))
                strip.setPixelColor(3, Color(255, 255, 255,))
                strip.show()

    except Exception as e:
            print(e.message)
        
def clear():
    try:
        strip.setPixelColor(0, Color(0, 0, 0, 0)) #None
        strip.setPixelColor(1, Color(0, 0, 0, 0))
        strip.setPixelColor(2, Color(0, 0, 0, 0))
        strip.setPixelColor(3, Color(0, 0, 0, 0))
        strip.show()
        print("Led's cleared")
        
    except Exception as e:
        print(e.message)
