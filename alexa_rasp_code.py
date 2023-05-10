import logging
import os
import multiprocessing

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']
STATUSOFF = ['off','low']

startcommandlist = ['start the autonomous system mode', 'turn on the autonomous system mode']
stopcommandlist = ['stop the autonomous system mode', 'turn off the autonomous system mode']
chargingdocklist = ['go to the charging dock', 'go to the charging station']
moveleftlist = ['move to the left', 'move left', 'go left']
moverightlist = ['move to the right', 'go right', 'move right']
movestraightlist = ['go straight', 'move straight']
comebacklist = ['come back', 'come to me']


# # Create a shared value of type int
# shared_value = multiprocessing.Value('i', 0)

# # to create an event object
# update_event = multiprocessing.Event()



@ask.launch
def launch():
    speech_text = 'Welcome to Raspberry Pi Automation.'

    return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.intent('StartAutonomousSystemIntent', mapping = {'STARTCOMMAND': 'STARTCOMMAND'})
def StartAutonomousSystemIntent(STARTCOMMAND):
    #StoreValue = "0"

    # Create a shared value of type int
    shared_value = multiprocessing.Value('i', 0)

    # to create an event object
    update_event = multiprocessing.Event()

    # Update the shared value
    shared_value.value = 42

    print("Shared value: ", shared_value.value)

    # Set the event to signal that the value has been updated
    update_event.set()
    
    return statement("Starting the autonomous system mode from the script!")
    # if STARTCOMMAND in startcommandlist:
    #     return statement(STARTCOMMAND)


@ask.intent('StopAutonomousSystemIntent', mapping = {'STOPCOMMAND': 'STOPCOMMAND'})
def StartAutonomousSystemIntent(STOPCOMMAND):
    StoreValue = "1"
    
    # update the shared value
    shared_value.value = 1

    # set the event to signal that the value has been updated
    update_event.set()

    return statement("Stopping the autonomous system mode from the script!!")



@ask.intent('ChargingDockIntent', mapping = {'CHARGINGCOMMAND': 'CHARGINGCOMMAND'})
def StartAutonomousSystemIntent(CHARGINGCOMMAND):

    # update the shared value
    shared_value.value = 2

    # set the event to signal that the value has been updated
    update_event.set()

    return statement("Going to the charging dock from the script!")



@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.default_intent
def default_intent():
    speech_text = "Sorry, I didn't understand what you said. Please try again."
    return statement(speech_text).simple_card('Error', speech_text)



@ask.session_ended
def session_ended():
    return "{}", 200





if __name__ == '__main__':
    # if 'ASK_VERIFY_REQUESTS' in os.environ:
    #     verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
    #     print("Verify: ", verify)
    #     if verify == 'false':
    #         app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)