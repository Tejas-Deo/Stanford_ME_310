import RPi.GPIO as GPIO
import time, sys
from voice_test import return_command
from ultrasonic_sensor_code import return_distances



ultr_sensor = return_distances()

while True:

	# to get the distances from the sensor


	# to get the user commands
	final_command = return_command()
	print("FINAL COMMAND: ", final_command)
	print()

	# to get the distances from all the ultrasonic sensors
	dist1 = ultr_sensor.distance_1()
	dist2 = ultr_sensor.distance_2()
	dist3 = ultr_sensor.distance_3()

	time.sleep(0.5)



sys.exit()

# set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# to define the motor pins
motor1A = 8
motor1B = 7
# motor1E = 25
motor2A = 1
motor2B = 12
#motor2E = 22

# encoder_A_1 = 18
# encoder_B_1 = 23
# encoder_A_2 = 24
# encoder_B_2 = 25

# to set up motor pins as output
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
# GPIO.setup(motor1E, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
#GPIO.setup(motor2E, GPIO.OUT)



#to control the motor direction
def motor1(direction):
	print("Inside motor 1....")
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
	print("Inside Motor 2...")
	if direction == "forward":
		GPIO.output(motor2A, GPIO.HIGH)
		GPIO.output(motor2B, GPIO.LOW)
	elif direction == "reverse":
		GPIO.output(motor2A, GPIO.LOW)
		GPIO.output(motor2B, GPIO.HIGH)
	else:
		GPIO.output(motor2A, GPIO.LOW)
		GPIO.output(motor2B, GPIO.LOW)


# def read_encoder():
#     prev_value = GPIO.input(encoder_A_1)
#     while True:
#         current_value = GPIO.input(encoder_A_1)
#         if current_value != prev_value:
#             count += 1
#             prev_value = current_value
#             print("Encoder count:", count)
#         time.sleep(0.001)


i = 0

while True:
	#print("Sending commands: ")
	motor1("reverse")
	motor2("forward")
	i = i + 1

	# if i == 100:
	# 	break


# stop the mnotors and clean up GPIO pins
# p1.stop()
# p2.stop()
#GPIO.cleanup()






