import RPi.GPIO as GPIO
import time

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
    #To calculate the distance from the object in "cm". Sound travels at a speed of 343 meters per second i.e. 0.0343 cm per microsecond. And then dividing the total distance travelled by 2 we get 0.01715 cm/us
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
