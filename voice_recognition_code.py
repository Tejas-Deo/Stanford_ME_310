import RPi.GPIO as GPIO
import time
import serial
import speech_recognition as sr
import webbrowser as wb
#from fuzzywuzzy import fuzz




import time, os, sys, contextlib

@contextlib.contextmanager
def ignoreStderr():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)



with ignoreStderr():
    '''
    Just writing a code block for speech recognition
    '''
    try:
        # Define the list of valid commands
        valid_commands = ["Hey Walker Go away", "Hey walker go to the charging dock", "Hey walker Come back", 
                        "Hey walker Start the autonomous system mode"]

        # Define the minimum confidence threshold for a valid command match
        min_confidence = 70
        print("Please speak: ")
        r = sr.Recognizer()
        mic = sr.Microphone()


        while True:
            with mic as source:
                # listen for 5 seconds and create the ambient noise energy level
                #r.adjust_for_ambient_noise(source, duration=5)
                audio = r.listen(source)

            
            words = r.recognize_google(audio, language = 'en-IN', show_all = True)
            print(words)
            # if words is not None:
            #     output = words[0]
            #     transcript = output["transcript"]
            #     print(transcript)
            #     print()
            # else:
            #     continue

            if words['alternative'] is not None:
                first_transcript = words['alternative'][0]['transcript']
                print("First transcript: ", first_transcript)

            # '''
            # To match the recognized commands to a list of valid commands
            # '''
            # best_match = None
            # best_match_confidence = 0

            # for command in valid_commands:
            #     confidence = fuzz.ratio(words.lower(), command.lower())
            #     if confidence > best_match_confidence:
            #         best_match = command
            #         best_match_confidence = confidence
            
            # # to exdcute the command if the confidence level is above a certain threshold
            # if best_match_confidence >= min_confidence:
            #     if words == "Go away":
            #         print(words)
            #     if words == "Park":
            #         print(words)
           
            #     if words == "Come back":
            #         print(words)
            #     if words == "Start autonomous system mode":
            #         print(words)
    
    except Exception as e:
        pass
