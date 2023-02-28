import hebi
from pynput import keyboard
from pynput.keyboard import Key, Controller, Listner
import numpy as np
import math
from time import sleep
from std_msgs.msg import Float64, Float64MultiArray
from sensor_msgs.msg import Joy
import rospy
import sleep



class Hebi_Robot:

    def __init__(self, family_name, actuator_names, step_size):
        self.family = family
        self.actuator_names = actuator_names
        self.step_size = step_size

        # to look for modules and get the family names
        lookup = hebi.Lookup()
        self.group = lookup.get_group_from_names(family, actuator_names)

        # get the feedback
        self.group_feedback = hebi.GroupFeedback(group.size)

        # creating motor velocities list 
        self.motor_velocities = [0.0, 0.0, 0.0, 0.0]

        # to make the robot go straight
        self.directions = [1., 1., 1., 1.]

        # rate at which the robot should go ahead
        self.speed = 1

        print("Starting the script....")

        # Define the keyboard bindings
        self.keyboard_commands = {
            'up': 0,
            'down': 1,
            'left': 2,
            'right': 3
        }
    
        # to initialize the hebi group command
        group_command = hebi.GroupCommand(self.group.size)
        group_command.position = [0] * self.group.size

    
    def return_values(self):
        return self.motor_velocities, self.directions, self.speed, self.keyboard_commands

    
    def run_loop(self):
        # to move the motors through the keyboard
        while True:
            
            # to send the velocities to each motor
            for i in range(self.group.size):
                group_command.velocity[i] = motor_velocities[i]
            self.group.send_command(group_command)
            self.group.get_next_feedback(reuse_fbk=group_feedback)




class take_keyboard_input:

    def __init__(self, motor_velocities, directions, speed, keyboard_commands):
        self.motor_velocities = motor_velocities
        self.directions = directions
        self.speed = speed
        self.keyboard_commands = keyboard_commands

    # to get the command from the keyboard
    def on_press(key):
        try:
            if key == keyboard.Key.up:
                print('Up arrow key pressed')
                x = keyboard.Key.up
                x = str(x)
                x = x.split(".")[1]
                print("test: ", keyboard_commands[x])
                index = keyboard_commands[x]
                motor_velocities[index] = directions[index] * speed

            elif key == keyboard.Key.down:
                print('Down arrow key pressed')
                x = keyboard.Key.down
                x = str(x)
                x = x.split(".")[1]
                index = keyboard_commands[x]
                motor_velocities[index] = directions[index] * speed

            elif key == keyboard.Key.left:
                print('Left arrow key pressed')
                x = keyboard.Key.left
                x = str(x)
                x = x.split(".")[1]
                index = keyboard_commands[x]
                motor_velocities[index] = directions[index] * speed

            elif key == keyboard.Key.right:
                print('Right arrow key pressed')
                x = keyboard.Key.right
                x = str(x)
                x = x.split(".")[1]
                index = keyboard_commands[x]
                motor_velocities[index] = directions[index] * speed


        except AttributeError:
            print('A special key {0} has been pressed'.format(key))


    def on_release(key):
        if key == keyboard.Key.esc:
            print("Escaping the keyboard control......")
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



if __name__ == '__main__':

    family=['base','base', 'base', 'base']
    actuator_names=['front_left_leg','front_right_leg', 'back_left_leg', 'back_right_leg']
    step_size = 1

    # to initialize the Hebi motor class
    hebi = Hebi_Robot(family, actuator_names)
    motor_velocities, directions, speed, keyboard_commands = hebi.return_values()

    try:
        # to take the keyboard inputs
        take_keyboard_input(motor_velocities, directions, speed, keyboard_commands)
        # to run the Hebi Robot
        hebi.run_loop()

    except KeyboardInterrupt:
        print("Terminating node")
