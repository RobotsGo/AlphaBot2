import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

CTR = 7
A = 8
B = 9
C = 10
D = 11
BUZ = 4

def beep_on():
	GPIO.output(BUZ,GPIO.HIGH)
def beep_off():
	GPIO.output(BUZ,GPIO.LOW)
	
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(CTR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(A,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(B,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(C,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(D,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(BUZ,GPIO.OUT)

try:
	while True:
		if GPIO.input(CTR) == 0:
			beep_on();
			Ab.stop();
			print("center")
			while GPIO.input(CTR) == 0:
				time.sleep(0.01)
		elif GPIO.input(A) == 0:
			beep_on();
			Ab.forward();
			print("up")
			while GPIO.input(A) == 0:
				time.sleep(0.01)
		elif GPIO.input(B) == 0:
			beep_on();
			Ab.right();
			print("right")
			while GPIO.input(B) == 0:
				time.sleep(0.01)
		elif GPIO.input(C) == 0:
			beep_on();
			Ab.left();
			print("left")
			while GPIO.input(C) == 0:
				time.sleep(0.01)
		elif GPIO.input(D) == 0:
			beep_on();
			Ab.backward();
			print("down")
			while GPIO.input(D) == 0:
				time.sleep(0.01)
		else:
			beep_off();

except KeyboardInterrupt:
	GPIO.cleanup()