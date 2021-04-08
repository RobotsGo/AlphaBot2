#!/usr/bin/python

from bottle import get,request, route, run, static_file,template  
import time, threading
# sudo pip install rpi_ws281x
from rpi_ws281x import Adafruit_NeoPixel, Color
import socket #ip

# LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
strip.show()

rgb = 0
light_type = 'static'    #'static':静态 'breath':呼吸 'flash':闪烁

#访问文件根目录
@get("/")
def index():
    global rgb, light_type
    rgb = 0xffffff
    light_type = 'static'
    return static_file('index.html', './')

#网页上的静态文件需要做传输处理
@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./')
	
#POST方式获取Ajax传输过来的rgb值
@route('/rgb', method='POST')
def rgbLight():
    red = request.POST.get('red')
    green = request.POST.get('green')
    blue = request.POST.get('blue')
    #print('red='+ red +', green='+ green +', blue='+ blue)
    red = int(red)
    green = int(green)
    blue = int(blue)
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        global rgb
        rgb = (red<<16) | (green<<8) | blue

#POST方式获取Ajax传输过来的type值
@route('/lightType', method='POST')
def lightType():
    global light_type
    light_type = request.POST.get('type')
    print("lightType="+light_type)

#灯光循环检测控制
def lightLoop():
	global rgb, light_type
	flashTime = [0.3, 0.2, 0.1, 0.05, 0.05, 0.1, 0.2, 0.5, 0.2] #闪烁时间间隔
	flashTimeIndex = 0 #闪烁时间间隔索引
	f = lambda x: (-1/10000.0)*x*x + (1/50.0)*x #用抛物线模拟呼吸灯
	x = 0
	while True:
		if light_type == 'static':   #静态显示
			for i in range(0,strip.numPixels()):
				strip.setPixelColor(i, rgb)     
			strip.show()
			time.sleep(0.05)
		elif light_type == 'breath': #闪烁显示
			red = int(((rgb & 0x00ff00)>>8) * f(x))
			green = int(((rgb & 0xff0000) >> 16) * f(x))
			blue = int((rgb & 0x0000ff) * f(x))
			_rgb = int((red << 8) | (green << 16) | blue)
			for i in range(0,strip.numPixels()):
				strip.setPixelColor(i, _rgb)     
				strip.show()
			time.sleep(0.02)
			x += 1
			if x >= 200:
				x = 0
		elif light_type == 'flash':  #呼吸灯显示
			for i in range(0,strip.numPixels()):
				strip.setPixelColor(i, rgb)     
				strip.show()
			time.sleep(flashTime[flashTimeIndex])
			for i in range(0,strip.numPixels()):
				strip.setPixelColor(i, 0)     
				strip.show()
			time.sleep(flashTime[flashTimeIndex])
			flashTimeIndex += 1
			if flashTimeIndex >= len(flashTime):
				flashTimeIndex = 0


#开辟新线程负责rgb灯光显示
t = threading.Thread(target = lightLoop)
t.setDaemon(True)
t.start()

#设置服务器ip地址和端口(提示：使用前请设置成你的树莓派ip地址)
# run(host="0.0.0.0", port=8002)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
localhost=s.getsockname()[0]
run(host = localhost, port = 8002)
