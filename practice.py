#!/usr/bin/env python

import rospy
import sys
import select
import tty
import termios
import hebi
from time import sleep
import math
import numpy as np



class take_keyboard_input:

    def __init__(self, motor_velocities, directions, speed, keyboard_commands):
        self.motor_velocities = motor_velocities
        self.directions = directions
        self.speed = speed
        self.keyboard_commands = keyboard_commands

        print("initialized the keyboard class....")
    

    # Define the main function
    def keyboard_main(self):
        # Initialize the ROS node
        rospy.init_node('keyboard_input')
        print("Initialized keyboard_input node.....")

        # Set the terminal settings to allow non-blocking keyboard input
        settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

        # Loop to read keyboard input and print it to the console
        while not rospy.is_shutdown():
            try:
                if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
                    # Read the keyboard input and convert it to a string
                    key = sys.stdin.read(1)
                    key_str = str(key)

                    print("Type: ", type(key_str))

                    # to use the keyboard input to move the robot
                    if key_str == "w":
                        print("Pressed \'w' key and going straight....")
                        index = self.keyboard_commands[key_str]
                        self.motor_velocities[index] = self.directions[index] * self.speed
                        return self.motor_velocities

                    if key_str == "s":
                        print("Pressed \'s' key and going reverse....")
                        index = self.keyboard_commands[key_str]
                        self.motor_velocities[index] = self.directions[index] * self.speed
                        return self.motor_velocities

                    if key_str == "a":
                        print("Pressed \'a' key and going left....")
                        index = self.keyboard_commands[key_str]
                        self.motor_velocities[index] = self.directions[index] * self.speed
                        return self.motor_velocities

                    if key_str == "d":
                        print("Pressed \'d' key and going right....")
                        index = self.keyboard_commands[key_str]
                        self.motor_velocities[index] = self.directions[index] * self.speed
                        return self.motor_velocities
                    
                    if key_str == "p":
                        print("Stopped taking inputs from the keyboard....")
                        break

                    # Print the keyboard input to the console
                    rospy.loginfo("Keyboard input: {}".format(key_str))

                    print("Returning the motor values.....")
                    #return self.motor_velocities

            except AttributeError:
                print('A special key {0} has been pressed'.format(key))

        # Restore the terminal settings before exiting
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)





# Call the main function
if __name__ == '__main__':

    #family=['base','base', 'base', 'base']
    #actuator_names=['front_left_leg','front_right_leg', 'back_left_leg', 'back_right_leg']

    # to initialize the Hebi motor class
    #hebi = Hebi_Robot(family, actuator_names)
    #motor_velocities, directions, speed, keyboard_commands = hebi.return_values()
    while True:
        # creating motor velocities list 
        motor_velocities = [0.0, 0.0, 0.0, 0.0]

        # to make the robot go straight
        directions = [1., 1., 1., 1.]

        # rate at which the robot should go ahead
        speed = 1

        # Define the keyboard bindings
        keyboard_commands = {
            'w': 0,
            's': 1,
            'a': 2,
            'd': 3
        }

        print("Starting the script....")

        # initialize the keyboard input class
        keyboard_class = take_keyboard_input(motor_velocities, directions, speed, keyboard_commands)
        # starting to take input from the keyboard
        motor_velocities = keyboard_class.keyboard_main()

        print("Motor velocity after keyboard command: ", motor_velocities)
        print("Sending motor velocities to the robot....")
        print()



        # to give the command to the robot
        #hebi.run_loop(motor_velocities)




