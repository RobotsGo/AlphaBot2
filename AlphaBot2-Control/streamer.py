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

from flask import Flask, render_template, Response
import io
import cv2
import psutil
from imutils import resize
import numpy as np

app = Flask(__name__)
vc = cv2.VideoCapture(0)
vc.set(cv2.CAP_PROP_FPS,30)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    while True:
        
        ret, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        
        font = cv2.FONT_HERSHEY_PLAIN
        logo = cv2.imread("rgLogo.png")
        stats = cv2.imread("overlay.png")
        logoResized = resize(logo, width=50, height=27)
        logoWaterMark = cv2.cvtColor(logoResized, cv2.COLOR_BGR2BGRA)
        statsHud = cv2.cvtColor(stats, cv2.COLOR_BGR2BGRA)
      
            #Get CPU temp in C
            
        temp = psutil.sensors_temperatures()
        for name, entries in temp.items():
            for entry in entries:
                cpuTemp = entry.current

    #Get total load CPU percentage
        cpuUsage = psutil.cpu_percent(interval=None, percpu=False)

    #Get memory usage percentage 
        mem = psutil.virtual_memory()
        memUsage = mem.percent

        ct = (str(int(cpuTemp)) + "C")
        cu = (str(cpuUsage) + "%")
        mu = (str(memUsage) + "%")
    
    #Inserting text on video
        cv2.putText(frame, cu, (65, 40), font, 1.5, (0, 0, 0), 2, cv2.LINE_4)
        cv2.putText(frame, ct, (198, 40), font, 1.5, (0, 0, 0), 2, cv2.LINE_4)
        cv2.putText(frame, mu, (325, 40), font, 1.5, (0, 0, 0), 2, cv2.LINE_4)
    
    #Build overlay for logo i = X, j = Y
        frame_h, frame_w, frame_c = frame.shape
        overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')*255
        
        logoWaterMark_h, logoWaterMark_w, logoWaterMark_c = logoWaterMark.shape
        for i in range(0, logoWaterMark_h):
            for j in range(0, logoWaterMark_w):
                if logoWaterMark[i, j][3] != 0:
                    overlay[i + 420, j + 580] = logoWaterMark[i, j]
                    
        #Build overlay for logo i = X, j = Y
        statsHud_h, statsHud_w, statsHud_c = statsHud.shape
        for i in range(0, statsHud_h):
            for j in range(0, statsHud_w):
                if statsHud[i, j][3] != 0:
                    overlay[i + 0, j + 0] = statsHud[i, j]
                    
        cv2.addWeighted(frame, 1, overlay, 1, 0, frame)
        
        encode_return_code, image_buffer = cv2.imencode('.jpg', frame)
        io_buf = io.BytesIO(image_buffer)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + io_buf.read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        gen(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )
    
if __name__ == '__main__':
    app.run(host=HOST_IP, debug=False, threaded=True)
