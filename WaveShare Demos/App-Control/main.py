import time
import subprocess
import threading
import SocketServer 
import RPi.GPIO as GPIO
from SocketServer import StreamRequestHandler as SRH  
from AlphaBot import AlphaBot
from PCA9685 import PCA9685
from time import ctime  
from rpi_ws281x import Adafruit_NeoPixel, Color


print("start")
# LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

DOT_COLORS = [  0xFF0000,   # red
				0xFF7F00,   # orange
				0xFFFF00,   # yellow
				0x00FF00,   # green
				0x00FFFF,   # lightblue
				0x0000FF,   # blue
				0xFF00FF,   # purple
				0xFF007F ]  # pink
				
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.setBrightness(50)
strip.begin()
strip.show()
offset = 0
count = 0
flag = 1


Ab = AlphaBot()
pwm = PCA9685(0x40)
pwm.setPWMFreq(50)

BUZ = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZ,GPIO.OUT)

#Set the Horizontal servo parameters
HPulse = 1500  #Sets the initial Pulse
HStep = 0      #Sets the initial step length
pwm.setServoPulse(0,HPulse)

#Set the vertical servo parameters
VPulse = 1500  #Sets the initial Pulse
VStep = 0      #Sets the initial step length
pwm.setServoPulse(1,VPulse)

time.sleep(5)
cmd = "hostname -I | cut -d\' \' -f1"
host = subprocess.check_output(cmd,shell = True )
print(host)
#host = '192.168.6.107'
port = 8000
addr = (host,port)  

def beep_on():
	GPIO.output(BUZ,GPIO.HIGH)
def beep_off():
	GPIO.output(BUZ,GPIO.LOW)

def setColor(color):
	for i in range(LED_COUNT):
		# Set the LED color buffer value.
		strip.setPixelColor(i, color)

	# Send the LED color data to the hardware.
	strip.show()
	
class Servers(SRH): 
	def handle(self): 
		global HStep,VStep,flag 
		print 'got connection from ',self.client_address  
		self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
		while True:  
			data = self.request.recv(1024)  
			if not data:   
				break  
			if data == "Stop":
				HStep = 0
				VStep = 0
				Ab.stop()
                                flag = 1
			elif data == "Forward":
                                flag = 0
				Ab.forward()
				setColor(0xFF0000)
			elif data == "Backward":
				flag = 0
                                Ab.backward()
				setColor(0xFFFF00)
			elif data == "TurnLeft":
				flag = 0
                                Ab.left()
				setColor(0x00FF00)
			elif data == "TurnRight":
				flag = 0
                                Ab.right()
				setColor(0x0000FF)
			elif data == "Up":
				VStep = -5
			elif data == "Down":
				VStep = 5
			elif data == "Left":
				HStep = 5
			elif data == "Right":
				HStep = -5
			elif data == "BuzzerOn":
				beep_on()
			elif data == "BuzzerOff":
				beep_off()
			else:
				value = 0
				try:
					value = int(data)
					if(value >= 0 and value <= 100):
						print(value)
						Ab.setPWMA(value);
						Ab.setPWMB(value);
				except:
					print("Command error")
			print data   
			#print "recv from ", self.client_address[0]  
			self.request.send(data)  
			
def timerfunc():
	global HPulse,VPulse,HStep,VStep,pwm,offset,count,flag
	
	if(HStep != 0):
		HPulse += HStep
		if(HPulse >= 2500): 
			HPulse = 2500
		if(HPulse <= 500):
			HPulse = 500
		#set channel 2, the Horizontal servo
		pwm.setServoPulse(0,HPulse)    
		
	if(VStep != 0):
		VPulse += VStep
		if(VPulse >= 2500): 
			VPulse = 2500
		if(VPulse <= 500):
			VPulse = 500
		#set channel 3, the vertical servo
		pwm.setServoPulse(1,VPulse)   
		# Update each LED color in the buffer.
	
	count += 1
	if(count > 10 and flag):
		for i in range(LED_COUNT):
			# Pick a color based on LED position and an offset for animation.
		        color = DOT_COLORS[(i + offset) % len(DOT_COLORS)]

	                # Set the LED color buffer value.
		        strip.setPixelColor(i, color)

	        # Send the LED color data to the hardware.
		strip.show()

		# Increase offset to animate colors moving.  Will eventually overflow, which
		# is fine.
		offset += 1
		count = 0
	
	global t        #Notice: use global variable!
	t = threading.Timer(0.02, timerfunc)
	t.start()
	
t = threading.Timer(0.02, timerfunc)
t.setDaemon(True)
t.start()

print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr,Servers)  
server.serve_forever()  
