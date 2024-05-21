# WEBROVER-Raspberry-Pi-Robot-with-Web-Control
Stream live video from your Raspberry Pi robot to a webpage, featuring intuitive control buttons for remote operation.

## Overview
WebRover is an innovative project that integrates modern technology components to create a dynamic and interactive robotic system. At its core, the project features a Raspberry Pi-powered mobile robot that can be controlled and monitored through a web interface. The system includes live video streaming, intuitive control buttons, and Twilio-based communication for remote access.

## Features
- **Live Video Streaming**: Real-time video feed from the robot's camera using OpenCV.
- **Remote Control**: Navigate the robot using a web interface with buttons for movement.
- **Twilio Integration**: Sends the robot's IP address and port number to the user via SMS.
- **User Authentication**: Secures access to the control interface with username and password.

## Hardware Requirements
- Raspberry Pi 4
- Micro SD Card
- Mobile Robot (e.g., Cherokey 4WD)
- Web Camera
- Jumper Wires

## Software Requirements
- Python 3
- Flask
- OpenCV (cv2)
- RPi.GPIO
- Twilio
- Socket.IO

## Installation and Setup

### 1. Configuring Raspberry Pi
1. **Install Raspberry Pi OS**:
   - Use Raspberry Pi Imager to install Raspberry Pi OS on your microSD card.
   - Configure the OS for remote access, set hostname, username, and enable SSH.

2. **Connect to WiFi**:
   - Set up the wireless LAN during the Raspberry Pi OS configuration.

### 2. Setting Up Twilio
1. **Create a Twilio Account**:
   - Sign up at Twilio and verify your email and phone number.
   - Obtain your Twilio Account SID, Auth Token, and a Twilio phone number.

### 3. Installing Dependencies
```bash
pip install flask opencv-python twilio RPi.GPIO python-socketio

### 3. Running the application
```bash
git clone https://github.com/yourusername/WebRover.git
cd WebRover

