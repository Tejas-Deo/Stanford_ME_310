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
            print(words)
        if words == "Park":
            print(words)
        if words == "Come back":
            print(words)
        if words == "Start autonomous system mode":
            print(words)


