import RPi.GPIO as GPIO
import time

# set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# to define the motor pins
motor1A = 23
motor1B = 24
motor1E = 25
motor2A = 17
motor2B = 27
motor2E = 22

# to set up motor pins as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor1E, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
GPIO.setup(motor2E, GPIO.OUT)

# setting up motor speed to 50%
p1 = GPIO.PWM(motor1E, 50)
p1.start(0)
p2 = GPIO.PWM(motor2E, 50)
p2.start(0)


# to control the motor direction
def motor1(direction):
	if direction == "forward":
		GPIO.output(motor1A, GPIO.HIGH)
		GPIO.output(motor1B, GPIO.LOW)
	elif direction == "reverse":
		GPIO.output(motor1A, GPIO.LOW)
		GPIO.output(motor1B, GPIO.HIGH)
	else:
		GPIO.output(motor1A, GPIO.LOW)
		GPIO.output(motor1B, GPIO.LOW)


def motor2(direction):
	if direction == "forward":
		GPIO.output(motor2A, GPIO.HIGH)
		GPIO.output(motor2B, GPIO.LOW)
	elif direction == "reverse":
		GPIO.output(motor2A, GPIO.LOW)
		GPIO.output(motor2B, GPIO.HIGH)
	else:
		GPIO.output(motor2A, GPIO.LOW)
		GPIO.output(motor2B, GPIO.LOW)


# function to control the motor speed
def set_speed1(speed):
	p1.CHangeDutyCycle(speed)

def set_speed2(speed):
	p2.CHangeDityCycle(speed)
	

# to test the motors by rotating them forward and backward at different speeds
motor1("forward")
motor2("forward")
set_speed1(50)
set_speed2(50)
time.sleep(20)



# stop the mnotors and clean up GPIO pins
p1.stop()
p2.stop()
GPIO.cleanup()
