import hebi
from time import sleep
import keyboard
import numpy as np
import pandas as pd
import time
import sys

lookup = hebi.Lookup()
# Give the Lookup process 2 seconds to discover modules
sleep(2)


# velocity is in rad/sec
vel = 2.0
radius = 0.2286
sideways_velocity = 2.0

fam_actuator_dict = dict()

family = []
names = []
for entry in lookup.entrylist:
    family += [entry.family]
    names += [entry.name]

group = lookup.get_group_from_names(family, names)


for fam_name, name in zip(family, names):
    fam_actuator_dict[fam_name] = name

print(fam_actuator_dict)


if group is None:
    print("Could not find the HEBI actuators")
    exit(1)

# # to create a dictionary with actuator_names and the corresponding velocity values
# name_index_dict = {
#     'back_right_leg':0,
#     'front_right_leg':1,
#     'back_left_leg':2,
#     'front_left_leg':3
# }

print("The order of actuator family and names is as follows:-")
for fam, name in zip(family, names):
    print(fam, name)


# print("Printing actuator name and index dicitonary..")
# print(name_index_dict)


# get the feedback
group_feedback = hebi.GroupFeedback(group.size)


# Define the keyboard bindings
keyboard_commands = {
    'w': 0,
    's': 1,
    'a': 2,
    'd': 3
}

group.start_log("logs", mkdirs = True)
print('Start giving commands....')

position = np.zeros(4)
last_time = 0.0

print("Printing initial position: ", group_feedback.position)

start_time = time.time()


angular_velocity_list = []
time_list = []
distance_travlled_list = []

print()
print("Printing names: ", names)

print("Exiting the system....")
#sys.exit()

while True:

    group_command = hebi.GroupCommand(group.size)

    # going straight
    if keyboard.is_pressed("w"):
        print("Going forward....")
        direction = np.array([1., -1., 1., -1.])
        velocity = direction * vel
        group_command.velocity = velocity
        group.send_command(group_command)
        #group.get_next_feedback(reuse_fbk=group_feedback)

        group_next_feedback = group.get_next_feedback(reuse_fbk= group_feedback)

        velocity_returned = group_next_feedback.velocity
        angular_velocity_list.append(velocity_returned)
        linear_velocity = velocity_returned * radius

        velocity_returned = group_next_feedback.velocity
        print("Printing the linear velocity returned....")
        print(linear_velocity)
        print()

        position = group_next_feedback.position

        print("Position: ")
        print(position)

    # going reverse
    if keyboard.is_pressed("s"):

        print("Going reverse....")
        direction = np.array([-1., 1., -1., 1.])
        velocity = direction * vel
        group_command.velocity = velocity
        group.send_command(group_command)
        #group.get_next_feedback(reuse_fbk=group_feedback)

        group_next_feedback = group.get_next_feedback(reuse_fbk= group_feedback)

        temp = np.zeros(4)

        print("getting the linear and anhgyular velocity...")
        velocity_returned = group_next_feedback.velocity
        angular_velocity_list.append(velocity_returned)
        linear_velocity = velocity_returned * radius
        print("Printing the linear velocity returned....")
        print(linear_velocity)
        print()

        gyro = group_next_feedback.gyro
        position = group_next_feedback.position

        print("Position: ")
        print(position)


    # turning left
    if keyboard.is_pressed("a"):
        print("Going left....")
        group_next_feedback = group.get_next_feedback(reuse_fbk= group_feedback)
        linear_velocity = velocity * radius
        angular_velocity = velocity 

        # to set the velocities for each actuator
        for module_name in names:
            if module_name == "front_left_leg":
                print("Sent command to the front_left_leg...")
                index = fam_actuator_dict[module_name]
                front_left_leg_vel = linear_velocity - angular_velocity/2
                group_command[index].velocity = front_left_leg_vel
                
                
            if module_name == "back_left_leg":
                print("Sent command to back_left_leg.....")
                index = fam_actuator_dict[module_name]
                back_left_leg_vel = linear_velocity - angular_velocity/2
                group_command[index].velocity = back_left_leg_vel
                

            if module_name == "front_right_leg":
                print("Sent command to front_right_leg.....")
                index = fam_actuator_dict[module_name]
                front_right_leg_vel = linear_velocity + angular_velocity/2
                group_command[index].velocity = front_right_leg_vel
                

            if module_name == "back_right_leg":
                print("Sent commad to back_right_leg.....")
                index = fam_actuator_dict[module_name]
                back_right_leg_vel = linear_velocity + angular_velocity/2
                group_command[index].velocity = back_right_leg_vel
                
            
        # to command the velocities to the actuator
        group.send_command(group_command)
    

    # turning right
    if keyboard.is_pressed("d"):
        print("Going right....")
        # set the velocity command to move the wheels in the left direction
        group_command.velocity = [-sideways_velocity, sideways_velocity, -sideways_velocity, sideways_velocity]

        # rotate the wheels first to move forward in the desired direction
        group_command.velocity[0] = group_command.velocity[0] - velocity
        group_command.velocity[1] = group_command.velocity[1] - velocity
        group_command.velocity[2] = group_command.velocity[2] + velocity
        group_command.velocity[3] = group_command.velocity[3] + velocity

        # to send the command to the actuators
        group.send_command(group_command)



end_time = time.time()

time_elapsed = end_time - start_time




    # if keyboard.is_pressed("q"):
    #     print("Breaking the while loop....")
    #     break


































'''
import hebi
from time import sleep
import numpy as np

lookup = hebi.Lookup()
# Give the Lookup process 2 seconds to discover modules
sleep(2)

print("Starting the script....")

# velocity is in radians per second
vel = 50.0

family = []
names = []
for entry in lookup.entrylist:
    family += [entry.family]
    names += [entry.name]

for fam, name in zip(family, names):
    print(fam, name)


# final order --> ["back_left_leg", "back_right_leg", "front_right_leg", "front_left_leg"]

group = lookup.get_group_from_names(family, names)
direction = np.array([1., -1., 1., -1.])
velocity = direction * vel

print(names)
print(velocity)


while True:
    key_inp = input("Give Direction: ")

    group_command = hebi.GroupCommand(group.size)

    if key_inp == 'w':
        group_command.velocity = velocity
        group.send_command(group_command)
    
    elif key_inp == 'q':
        break
'''