import logging
import os

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

# @ask.launch
# def launch():
#     speech_text = 'Welcome to Raspberry Pi Automation.'
#     return question(speech_text).reprompt(speech_text).simple_card(speech_text)


@ask.intent('StartAutonomousSystemIntent', mapping = {'STARTCOMMAND': 'STARTCOMMAND'})
def StartAutonomousSystemIntent(STARTCOMMAND):
    if STARTCOMMAND in startcommandlist:
        return statement(STARTCOMMAND)


@ask.intent('StopAutonomousSystemIntent', mapping = {'STOPCOMMAND': 'STOPCOMMAND'})
def StartAutonomousSystemIntent(STOPCOMMAND):
    if STOPCOMMAND in stopcommandlist:
        return statement(STOPCOMMAND)


@ask.intent('ChargingDockIntent', mapping = {'CHARGINGCOMMAND': 'CHARGINGCOMMAND'})
def StartAutonomousSystemIntent(CHARGINGCOMMAND):
    if CHARGINGCOMMAND in chargingdocklist:
        return statement(CHARGINGCOMMAND)


@ask.intent('MoveLeftIntent', mapping = {'LEFTCOMMAND': 'LEFTCOMMAND'})
def StartAutonomousSystemIntent(LEFTCOMMAND):
    if LEFTCOMMAND in moveleftlist:
        return statement(LEFTCOMMAND)


@ask.intent('MoveRightIntent', mapping = {'RIGHTCOMMAND': 'RIGHTCOMMAND'})
def StartAutonomousSystemIntent(RIGHTCOMMAND):
    if RIGHTCOMMAND in moverightlist:
        return statement(RIGHTCOMMAND)


@ask.intent('GoStraightIntent', mapping = {'STRAIGHTCOMMAND': 'STRAIGHTCOMMAND'})
def StartAutonomousSystemIntent(STRAIGHTCOMMAND):
    if STRAIGHTCOMMAND in movestraightlist:
        return statement(STRAIGHTCOMMAND)


@ask.intent('ComeBackIntent', mapping = {'COMEBACKCOMMAND': 'COMEBACKCOMMAND'})
def StartAutonomousSystemIntent(COMEBACKCOMMAND):
    if COMEBACKCOMMAND in comebacklist:
        return statement(COMEBACKCOMMAND)



# @ask.intent('GpioIntent', mapping = {'status':'status'})
# def Gpio_Intent(status,room):
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)    
#     GPIO.setup(17,GPIO.OUT)
#     if status in STATUSON:
#         GPIO.output(17,GPIO.HIGH)
#         return statement('turning {} lights'.format(status))
#     elif status in STATUSOFF:
#         GPIO.output(17,GPIO.LOW)
#         return statement('turning {} lights'.format(status))
#     else:
#         return statement('Sorry not possible.')


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)