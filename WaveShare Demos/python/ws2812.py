# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from rpi_ws281x import Adafruit_NeoPixel, Color

# LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Create NeoPixel object with appropriate configuration.
# Intialize the library (must be called once before other functions).
strip.begin()
strip.setPixelColor(0, Color(255, 0, 0))       #Red
strip.setPixelColor(1, Color(0, 255, 0))       #Green
strip.setPixelColor(2, Color(0, 0, 255))       #Blue
strip.setPixelColor(3, Color(255, 255, 0))     #Yellow
strip.show()

time.sleep(2)
strip.setPixelColor(0, Color(0, 0, 0))       #Red
strip.setPixelColor(1, Color(0, 0, 0))       #Green
strip.setPixelColor(2, Color(0, 0, 0))       #Blue
strip.setPixelColor(3, Color(0, 0, 0))       #Yellow
strip.show()


