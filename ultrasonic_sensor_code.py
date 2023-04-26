#Libraries
import RPi.GPIO as GPIO
import time


class return_distances:

    def __init__(self):

        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        
        #set GPIO Pins for sensor 1
        self.GPIO_TRIGGER_1 = 15
        self.GPIO_ECHO_1 = 14

        # set GPIO Pins for sensor 2
        self.GPIO_TRIGGER_2 = 21
        self.GPIO_ECHO_2 = 20

        # set GPIO Pins for sensor 3
        self.GPIO_TRIGGER_3 = 16
        self.GPIO_ECHO_3 = 26
        

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER_1, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO_1, GPIO.IN)

        GPIO.setup(self.GPIO_TRIGGER_2, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO_2, GPIO.IN)

        GPIO.setup(self.GPIO_TRIGGER_3, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO_3, GPIO.IN)


        def distance_1():
            '''
            To calculate the distance for the first sensor
            '''
            # set Trigger to HIGH
            GPIO.output(self.GPIO_TRIGGER_1, True)

            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER_1, False)

            StartTime_1 = time.time()
            StopTime_1 = time.time()
        
            # save StartTime
            while GPIO.input(self.GPIO_ECHO_1) == 0:
                StartTime_1 = time.time()
        
            # save time of arrival
            while GPIO.input(self.GPIO_ECHO_1) == 1:
                StopTime_1 = time.time()
        
            # time difference between start and arrival
            TimeElapsed_1 = StopTime_1 - StartTime_1
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance_1 = (TimeElapsed_1 * 34300) / 2
        
            return distance_1



        def distance_2():

            '''
            To calculate the distance for the second sensor
            '''
            # set Trigger to HIGH
            GPIO.output(self.GPIO_TRIGGER_2, True)

            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER_2, False)

            StartTime_2 = time.time()
            StopTime_2 = time.time()
        
            # save StartTime
            while GPIO.input(self.GPIO_ECHO_2) == 0:
                StartTime_2 = time.time()
        
            # save time of arrival
            while GPIO.input(self.GPIO_ECHO_2) == 1:
                StopTime_2 = time.time()
        
            # time difference between start and arrival
            TimeElapsed_2 = StopTime_2 - StartTime_2
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance_2 = (TimeElapsed_2 * 34300) / 2
        
            return distance_2



        def distance_3():

            '''
            To calculate the distance for the second sensor
            '''
            # set Trigger to HIGH
            GPIO.output(self.GPIO_TRIGGER_3, True)

            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER_3, False)

            StartTime_3 = time.time()
            StopTime_3 = time.time()
        
            # save StartTime
            while GPIO.input(self.GPIO_ECHO_3) == 0:
                StartTime_3 = time.time()
        
            # save time of arrival
            while GPIO.input(self.GPIO_ECHO_3) == 1:
                StopTime_3 = time.time()
        
            # time difference between start and arrival
            TimeElapsed_3 = StopTime_3 - StartTime_3
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance_3 = (TimeElapsed_3 * 34300) / 2
        
            return distance_3




# if __name__ == '__main__':
#     try:
#         while True:
#             dist1 = distance_1()
#             dist2 = distance_2()
#             dist3 = distance_3()
#             print("Distance 1, 2, and 3 are: ", dist1, dist2, dist3)
#             #print ("Measured Distance = %.1f cm" % dist)
#             time.sleep(1)
 
#         # Reset by pressing CTRL + C
#     except KeyboardInterrupt:
#         print("Measurement stopped by User")
#         GPIO.cleanup()































# import RPi.GPIO as GPIO
# import time

# '''
# Define GPIO pins for the 3 ultrasonic sensors
#  '''
# TRIG_PIN_1 = 14
# ECHO_PIN_1 = 15
# # TRIG_PIN_2 = 14
# # ECHO_PIN_2 = 12
# # TRIG_PIN_3 = 18
# # ECHO_PIN_3 = 16

# # Set GPIO mode and pin numbering
# GPIO.setmode(GPIO.BCM)

# # Setting up the GPIO pins based for the ultrasonic sensors
# GPIO.setup(TRIG_PIN_1, GPIO.OUT)
# GPIO.setup(ECHO_PIN_1, GPIO.IN)

# # GPIO.setup(TRIG_PIN_2, GPIO.OUT)
# # GPIO.setup(ECHO_PIN_2, GPIO.IN)

# # GPIO.setup(TRIG_PIN_3, GPIO.OUT)
# # GPIO.setup(ECHO_PIN_3, GPIO.IN)


# '''
# Function which calculates the distance from each ultrasonic sensor. This is being called in a continuous while loop. This function returns the distance when queried for a particular ultrasonic sensor
# '''
# def distance(trig_pin, echo_pin):
#     # Send 10us pulse to trigger pin
#     print("Sending the trigger.....")
#     GPIO.output(trig_pin, True)
#     time.sleep(0.00001)
#     GPIO.output(trig_pin, False)

#     print("Trigger sent....")

#     # Measure pulse duration from echo pin
#     pulse_start = time.time()
#     while GPIO.input(echo_pin) == 0:
#         pulse_start = time.time()

#     pulse_end = time.time()
#     while GPIO.input(echo_pin) == 1:
#         pulse_end = time.time()

#     pulse_duration = pulse_end - pulse_start
#     print("Pulse duration: ", pulse_duration)

#     '''
#     #To calculate the distance from the object in "cm". Sound travels at a speed of 343 meters per second i.e. 0.0343 cm per microsecond. And then dividing the total distance travelled by 2 we get 0.01715 cm/us
#     '''
#     distance = pulse_duration * 17150
#     distance = round(distance, 2)

#     return distance



# # Main loop
# try:
#     while True:
#         print("Inside: ")
#         # Read distances from all sensors
#         distance_1 = distance(TRIG_PIN_1, ECHO_PIN_1)
#         # distance_2 = distance(TRIG_PIN_2, ECHO_PIN_2)
#         # distance_3 = distance(TRIG_PIN_3, ECHO_PIN_3)

#         print("Distance 1: ", distance_1)
#         # print("Distance 2: ", distance_2)
#         # print("Distance 3: ", distance_3)
#         print()

#         # # Check if any sensor detects obstacle within 15cm
#         # if distance_1 < 15 or distance_2 < 15 or distance_3 < 15:
#         #     # Stop the robot base
#         #     GPIO.output(IN1, GPIO.LOW)
#         #     print("Obstacle detected. Stopping the robot base.")
#         # else:
#         #     # Move the robot base forward
#         #     GPIO.output(IN1, GPIO.HIGH)
#         #     print("Moving the robot base forward.")       
        
            
#         time.sleep(1)


# except KeyboardInterrupt:
#     GPIO.cleanup()
