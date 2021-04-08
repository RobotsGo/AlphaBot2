#!/usr/bin/env python
from flask import Flask, render_template, Response
import io
import cv2
import psutil

app = Flask(__name__)
vc = cv2.VideoCapture(0)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    while True:
        
        read_return_code, frame = vc.read()
        
        FONT = cv2.FONT_HERSHEY_PLAIN
      
            #Get CPU temp in C
            
        temp = psutil.sensors_temperatures()
        for name, entries in temp.items():
            for entry in entries:
                CPU_TEMP = entry.current

    #Get total load CPU percentage
        CPU_USAGE = psutil.cpu_percent(interval=None, percpu=False)

    #Get memory usage percentage 
        MEM = psutil.virtual_memory()
        MEM_USAGE = MEM.percent

        CT = ("CPU Temp: " + str(round(CPU_TEMP, 1)) + "C")
        CU = ("CPU Usage: " + str(round(CPU_USAGE, 1)) + "%")
        MU = ("Memory Usage: " + str(round(MEM_USAGE,1 )) + "%")
        #SC = ("Selected Colour: " + SELECTED_COLOUR)
        
        # if MODE == 1:
            # SM = ("Selected Speed Mode: SLOW")
        # elif MODE == 2:
            # SM = ("Selected Speed Mode: MEDIUM")
        # elif MODE == 3:
            # SM = ("Selected Speed Mode: FAST")
        # else:
            # SM = ("Selected Speed Mode: SLOW")
    
    #inserting text on video
        cv2.putText(frame, CT, (15, 15), FONT, 1, (0, 255, 255), 1, cv2.LINE_4)
        cv2.putText(frame, CU, (15, 30), FONT, 1, (0, 255, 255), 1, cv2.LINE_4)
        cv2.putText(frame, MU, (15, 45), FONT, 1, (0, 255, 255), 1, cv2.LINE_4)
        #cv2.putText(frame, SC, (15, 60), FONT, 1, (0, 255, 255), 1, cv2.LINE_4)
        #cv2.putText(frame, SM, (15, 45), FONT, 1, (0, 255, 255), 1, cv2.LINE_4)
        
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
