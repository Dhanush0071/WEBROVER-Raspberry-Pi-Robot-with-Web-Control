from flask import Flask, render_template, request, Response
import cv2
import socket
import sys, tty, termios, os
import MDD10A as HBridge
import time
from twilio.rest import Client

speedleft = 0
speedright = 0

app = Flask(__name__)

# Hardcoded authentication details
#set your username and password here
USERNAME = "admin"
PASSWORD = "password"

# Video capture object

def gen_frames():
	cap=cv2.VideoCapture(0)
	while True:
		success, frame = cap.read()  # Read the camera frame
		if not success:
			break
		else:
			ret, buffer = cv2.imencode('.jpg', frame)
			frame = buffer.tobytes()
			yield (b'--frame\r\n'
				   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Send frame as JPEG data

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return render_template('stream.html')
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<direction>')
def move(direction):
	global speedleft
	global speedright
	if(direction == "up"):
		speedleft =  0.02
		speedright = 0.02
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)


	if(direction == "down"):
		speedleft = 0.02
		speedright = 0.02

		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)

	if(direction == "stop"):
		speedleft = 0
		speedright = 0
		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
		
	if(direction == "right"):
		speedright = -0.02
		speedleft = 0.02

		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)

	if(direction == "left"):
		speedleft = -0.02
		speedright = 0.02

		HBridge.setMotorLeft(speedleft)
		HBridge.setMotorRight(speedright)
	print(f"Button pressed: {direction}")
	return "Key pressed: " + direction

if __name__ == '__main__':
	account_sid='YOUR TWILIO ACCOUNT SID'
	auth_token='YOUR TWILIO AUTH TOKEN'
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip_address=s.getsockname()[0]
	s.close()
	msg="you can use your robot on"+" ip address : "+ip_address+'\n'+"Port no : "+"5000"
	client=Client(account_sid,auth_token)
	message=client.messages.create(from_='YOUR TWILIO VIRTUAL PHONE NUMBER',body=msg,to='RECEIVERS PHONE NUMBER')
	app.run(host=ip_address,port='5000',debug=True)
