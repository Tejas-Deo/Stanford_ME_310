#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import hebi
import keyboard
import numpy as np
import math
from std_msgs.msg import Float64, Float64MultiArray
import rospy
import sys
import select
import tty
import termios
import hebi
from time import sleep
import math
import numpy as np
from matplotlib import pyplot as plt

# to find the modules on the network
lookup = hebi.Lookup()

# to give 2 seconds to look for the modules
sleep(2)

print('The following modules are found:')
print("Printing lookup: ", lookup.entrylist)

for entry in lookup.entrylist:
    print(f'{entry.family} | {entry.name}')


family=['base','base', 'base', 'base']
actuator_names=['front_left_leg','front_right_leg', 'back_left_leg', 'back_right_leg']

# to look for modules and get the family names
# lookup = hebi.Lookup()
# for entry in lookup.entrylist:
#     print(f'{entry.family} | {entry.name}')


# to get the group names present on the network
group = lookup.get_group_from_names(family, actuator_names)

if group is None:
    print("Could not find the HEBI actuators")
    exit(1)

# get the feedback
group_feedback = hebi.GroupFeedback(group.size)

# creating motor velocities list 
motor_velocities = [0.0, 0.0, 0.0, 0.0]

# to make the robot go straight
directions = [1., 1., 1., 1.]

# rate at which the robot should move (rad/sec)
velocity = 2
sideways_velocity = 2

print("Starting the script....")
# Define the keyboard bindings
keyboard_commands = {
    'w': 0,
    's': 1,
    'a': 2,
    'd': 3
}

group.start_log("logs", mkdirs = True)


settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

rospy.init_node('keyboard_input')
print("Initialized keyboard_input node.....")


# Loop to read keyboard input and print it to the console
while not rospy.is_shutdown():

    try:
        
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            # Read the keyboard input and convert it to a string
            key = sys.stdin.read(1)
            key_str = str(key)

            group_command = hebi.GroupCommand(group.size)

            #print("Type: ", type(key_str))


            # to move robot in the forward direction
            if key_str == "w":
                print("Pressed \'w' key and going straight....")
                index = keyboard_commands[key_str]

                group_command.velocity = [velocity] * group.size
                group.send_command(group_command)
                group.get_next_feedback(reuse_fbk=group_feedback)


            # to move the robot in the backward direction
            if key_str == "s":
                print("Pressed \'s' key and going reverse....")
                index = keyboard_commands[key_str]

                group_command.velocity = [-velocity] * group.size
                group.send_command(group_command)
                group.get_next_feedback(reuse_fbk=group_feedback)

            
            # to move the robot in the left direction
            if key_str == "a":
                print("Pressed \'a' key and going left....")
                index = keyboard_commands[key_str]

                # set the velocity command to move the wheels in the left direction
                groud_command.velocity = [sideways_velocity, -sideways_velocity, sideways_velocity, -sideways_velocity]

                # rotate the wheels first to move forward in the desired direction
                groud_command.velocity[0] = groud_command.velocity[0] + velocity
                groud_command.velocity[1] = groud_command.velocity[1] + velocity
                groud_command.velocity[2] = groud_command.velocity[2] - velocity
                groud_command.velocity[3] = groud_command.velocity[3] - velocity

                # to send the command to the actuators
                group.send_command(group_command)


            # to move the robot in the right direction
            if key_str == "d":
                print("Pressed \'d' key and going right....")
                index = keyboard_commands[key_str]

                # set the velocity command to move the wheels in the left direction
                groud_command.velocity = [-sideways_velocity, sideways_velocity, -sideways_velocity, sideways_velocity]

                # rotate the wheels first to move forward in the desired direction
                groud_command.velocity[0] = groud_command.velocity[0] - velocity
                groud_command.velocity[1] = groud_command.velocity[1] - velocity
                groud_command.velocity[2] = groud_command.velocity[2] + velocity
                groud_command.velocity[3] = groud_command.velocity[3] + velocity

                # to send the command to the actuators
                group.send_command(groud_command)

            
            if key_str == "p":
                print("Stopped taking inputs from the keyboard....")
                break

            # if no key is being pressed then 0 velocity command is being sent
            else:
                groud_command.velocity = [0] * group.size
                group.send_command(group_command)

            # Print the keyboard input to the console
            rospy.loginfo("Keyboard input: {}".format(key_str))

            print("Returning the motor values.....")
            #return self.motor_velocities

    except AttributeError:
        print('A special key {0} has been pressed'.format(key))

# Restore the terminal settings before exiting
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)



# while True:
#     group_command = hebi.GroupCommand(self.group.size)
#     # to send the velocities to each motor
#     # for i in range(self.group.size):
#     #     group_command.velocity[i] = motor_velocities[i]
#     group_command.velocity = motor_velocities
#     self.group.send_command(group_command)
#     self.group.get_next_feedback(reuse_fbk=group_feedback)


if log_file is not None:
    hebi.util.plot_logs(log_file, position)