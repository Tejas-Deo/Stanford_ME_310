import hebi
import keyboard 
import numpy as np
import math
from time import sleep
from std_msgs.msg import Float64, Float64MultiArray
from sensor_msgs.msg import Joy
import rospy


family=['base','base', 'base', 'base']
actuator_names=['front_left_leg','front_right_leg', 'back_left_leg', 'back_right_leg']

# to look for modules and get the family names
lookup = hebi.Lookup()
group = lookup.get_group_from_names(family, actuator_names)

# get the feedback
group_feedback = hebi.GroupFeedback(group.size)

# Define the keyboard bindings
keyboard_commands = {
    'up': 0,
    'down': 1,
    'left': 2,
    'right': 3,
    'w': 4,
    's': 5
}


# creating motor velocities list 
motor_velocities = [0.0, 0.0, 0.0, 0.0]

# to make the robot go straight
directions = [1., 1., 1., 1.]

# rate at which the robot should go ahead
speed = 1


# Define the keyboard callback function
def on_press(event):
    if event.name in keyboard_commands:
        index = keyboard_commands[event.name]
        motor_velocities[index] = directions[index] * speed

def on_release(event):
    if event.name in keyboard_commands:
        index = keyboard_commands[event.name]
        motor_velocities[index] = 0


# Register the keyboard callbacks
keyboard.on_press(on_press)
keyboard.on_release(on_release)


# to move the motors through the keyboard
while True:
    group_command = hebi.GroupCommand(group.size)
    # to send the velocities to each motor
    for i in range(group.size):
        group_command.velocity[i] = motor_velocities[i]
    group.send_command(group_command)
    group.get_next_feedback(reuse_fbk=group_feedback)