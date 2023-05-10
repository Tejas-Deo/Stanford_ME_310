import logging
import os, time
import multiprocessing
import threading
from threading import Thread, Lock
#import paho.mqtt.client as mqtt

from paho.mqtt import client as mqtt_client

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


# Define broker information
broker_address = '192.168.10.132'
broker_port = 1883
broker_username = "avatar"
broker_password = "avatar"

client_id = "python-mqtt-test"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(broker_username, broker_password)
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client



def publish(client, topic, msg):

    result = client.publish(topic, msg)
    status = result[0]

    if status == 0:
        print("Published the message of {} topic".format(topic))
    else:
        print('Failed to publis the message to {} topic!!!!!'.format(topic))






@ask.launch
def launch():
    speech_text = 'Welcome to Raspberry Pi Automation.'

    return question(speech_text).reprompt(speech_text).simple_card(speech_text)





@ask.intent('StartAutonomousSystemIntent', mapping = {'STARTCOMMAND': 'STARTCOMMAND'})
def StartAutonomousSystemIntent(STARTCOMMAND):

    message = "Start Auto system: "

    client = connect_mqtt()
    client.loop_start()
    topic = "AutoSystem/Start"
    publish(client, topic, message)
    client.disconnect()

    print("Start message published.....")
    
    return statement("Starting the autonomous system mode from the script!")




@ask.intent('StopAutonomousSystemIntent', mapping = {'STOPCOMMAND': 'STOPCOMMAND'})
def StopAutonomousSystemIntent(STOPCOMMAND):
    StoreValue = "1"

    message = "Stop Auto system: "

    client = connect_mqtt()
    client.loop_start()
    topic = "AutoSystem/Stop"
    publish(client, topic, message)
    client.disconnect()

    #print("Stop Message published.....")

    return statement("Stopping the autonomous system mode from the script!!")





@ask.intent('ChargingDockIntent', mapping = {'CHARGINGCOMMAND': 'CHARGINGCOMMAND'})
def ChargingDockIntent(CHARGINGCOMMAND):

    message = "Go to the charging dock: "

    client = connect_mqtt()
    client.loop_start()
    topic = "AutoSystem/ChargingDock"
    publish(client, topic, message)
    client.disconnect()

    #print("Charging dock Message published....")

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