import RPi.GPIO as GPIO
import time
import serial
import speech_recognition as sr
from fuzzywuzzy import fuzz


'''
Just writing a code block for speech recognition
'''

# Define the list of valid commands
valid_commands = ["Go away", "Park", "Come back", "Start autonomous system mode"]

# Define the minimum confidence threshold for a valid command match
min_confidence = 70

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

    '''
    To match the recognized commands to a list of valid commands
    '''
    best_match = None
    best_match_confidence = 0

    for command in valid_commands:
        confidence = fuzz.ratio(words.lower(), command.lower())
        if confidence > best_match_confidence:
            best_match = command
            best_match_confidence = confidence
    
    # to exdcute the command if the confidence level is above a certain threshold
    if best_match_confidence >= min_confidence:
        if words == "Go away":
            pass
        if words == "Park":
            pass
        if words == "Come back":
            pass
        if words == "Start autonomous system mode":
            pass


'''
Define GPIO pins for the 3 ultrasonic sensors
'''
TRIG_PIN_1 = 23
ECHO_PIN_1 = 24

TRIG_PIN_2 = 17
ECHO_PIN_2 = 27

TRIG_PIN_3 = 20
ECHO_PIN_3 = 21

# Set GPIO mode and pin numbering
GPIO.setmode(GPIO.BCM)

# Setting up the GPIO pins based for the ultrasonic sensors
GPIO.setup(TRIG_PIN_1, GPIO.OUT)
GPIO.setup(ECHO_PIN_1, GPIO.IN)

GPIO.setup(TRIG_PIN_2, GPIO.OUT)
GPIO.setup(ECHO_PIN_2, GPIO.IN)

GPIO.setup(TRIG_PIN_3, GPIO.OUT)
GPIO.setup(ECHO_PIN_3, GPIO.IN)


# this is the pin number of the motor that drives the walker
IN1 = 18

# these are the pin numbers for the motors bring down the autonomous system assembly
IN2 = 15
IN3 = 14


# Setting up the main motor pins
GPIO.setup(IN1, GPIO.OUT)

# setting up the pins for actuating the assembly
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)


'''
Function which calculates the distance from each ultrasonic sensor. This is being called in a continuous while loop. This function returns the distance when queried for a particular ultrasonic sensor
'''
def distance(trig_pin, echo_pin):
    # Send 10us pulse to trigger pin
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    # Measure pulse duration from echo pin
    pulse_start = time.time()
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    '''
    To calculate the distance from the object in "cm". Sound travels at a speed of 343 meters per second i.e. 0.0343 cm per microsecond. And then dividing the total distance travelled by 2 we get 0.01715 cm/us
    '''
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance


# Main loop
try:
    while True:
        # Read distances from all sensors
        distance_1 = distance(TRIG_PIN_1, ECHO_PIN_1)
        distance_2 = distance(TRIG_PIN_2, ECHO_PIN_2)
        distance_3 = distance(TRIG_PIN_3, ECHO_PIN_3)

        # Check if any sensor detects obstacle within 15cm
        if distance_1 < 15 or distance_2 < 15 or distance_3 < 15:
            # Stop the robot base
            GPIO.output(IN1, GPIO.LOW)
            print("Obstacle detected. Stopping the robot base.")
        else:
            # Move the robot base forward
            GPIO.output(IN1, GPIO.HIGH)
            print("Moving the robot base forward.")
            
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
