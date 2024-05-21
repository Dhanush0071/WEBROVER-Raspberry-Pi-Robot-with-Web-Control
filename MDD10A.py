
#!/usr/bin/env python

# Import the libraries the class needs
import RPi.GPIO as io

# Set GPIO mode and pins
io.setmode(io.BCM)

# Constant values
PWM_MAX = 100

# Disable warning from GPIO
io.setwarnings(False)

# Define GPIO pins for motor control
leftMotor_DIR_pin = 22
io.setup(leftMotor_DIR_pin, io.OUT)

rightMotor_DIR_pin = 23
io.setup(rightMotor_DIR_pin, io.OUT)

io.output(leftMotor_DIR_pin, False)
io.output(rightMotor_DIR_pin, False)

leftMotor_PWM_pin = 17
rightMotor_PWM_pin = 18

io.setup(leftMotor_PWM_pin, io.OUT)
io.setup(rightMotor_PWM_pin, io.OUT)

# MAX Frequency 20 Hz
leftMotorPWM = io.PWM(leftMotor_PWM_pin, 1000)
rightMotorPWM = io.PWM(rightMotor_PWM_pin, 1000)

leftMotorPWM.start(0)
leftMotorPWM.ChangeDutyCycle(0)

rightMotorPWM.start(0)
rightMotorPWM.ChangeDutyCycle(0)

leftMotorPower = 0
rightMotorPower = 0

def getMotorPowers():
    return (leftMotorPower, rightMotorPower)

def setMotorLeft(power):
    global leftMotorPower
    if power < 0:
        io.output(leftMotor_DIR_pin, False)
        pwm = -int(PWM_MAX * power)
        if pwm > PWM_MAX:
            pwm = PWM_MAX
    elif power > 0:
        io.output(leftMotor_DIR_pin, True)
        pwm = int(PWM_MAX * power)
        if pwm > PWM_MAX:
            pwm = PWM_MAX
    else:
        io.output(leftMotor_DIR_pin, False)
        pwm = 0
    leftMotorPower = pwm
    leftMotorPWM.ChangeDutyCycle(pwm)

def setMotorRight(power):
    global rightMotorPower
    if power < 0:
        io.output(rightMotor_DIR_pin, True)
        pwm = -int(PWM_MAX * power)
        if pwm > PWM_MAX:
            pwm = PWM_MAX
    elif power > 0:
        io.output(rightMotor_DIR_pin, False)
        pwm = int(PWM_MAX * power)
        if pwm > PWM_MAX:
            pwm = PWM_MAX
    else:
        io.output(rightMotor_DIR_pin, False)
        pwm = 0
    rightMotorPower = pwm
    rightMotorPWM.ChangeDutyCycle(pwm)

def exit():
    io.output(leftMotor_DIR_pin, False)
    io.output(rightMotor_DIR_pin, False)
    io.cleanup()
