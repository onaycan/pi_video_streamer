from flask import Response
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils
from flask import Flask
import datetime
from flask import render_template
from flask_cors import CORS
import cv2
import threading
from flask import send_file
import time

#globals
outputFrame = None
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes
#vs = VideoStream(0).start()
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()
time.sleep(2.0)

def generate_frame():
    global outputFrame, fps
	# loop over frames from the output stream
    while fps._numFrames % 32 == 0:
        outputFrame = vs.read()
        outputFrame = imutils.resize(outputFrame, width=700)
        timestamp = datetime.datetime.now()
        (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
        
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_socket")
def video_socket():
    return Response(generate_frame(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")
    
if __name__ == '__main__':
	app.run(host="10.42.0.1", port="5500", ssl_context=('./certs/server.crt', './certs/server.key'), debug=True, use_reloader=False)

fps.stop()
vs.stop()