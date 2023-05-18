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
broker_address = '192.168.30.2'
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
        print('Failed to publish the message to {} topic!!!!!'.format(topic))



def subscribe(client: mqtt_client, topic):
    print("Inside the subscribe function...")
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        return msg.payload.decode()

    client.subscribe(topic)
    client.on_message = on_message





@ask.launch
def launch():
    speech_text = 'Welcome to Smart walker assistant from the script!'

    return question(speech_text).reprompt(speech_text).simple_card(speech_text)




@ask.intent('StartAutonomousSystemIntent', mapping = {'STARTCOMMAND': 'STARTCOMMAND'})
def StartAutonomousSystemIntent(STARTCOMMAND):

    statement("Starting the autonomous system mode from the script!")

    # to deifne the message to be sent to the MQTT Broker
    message = "StartAuto"

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    while True:
        microcontroller_response = subscribe(client, topic)

        if microcontroller_response is not None:
            statement (microcontroller_response)
            break

    client.disconnect()

    print("Start message published.....")
    
    return None




@ask.intent('StopAutonomousSystemIntent', mapping = {'STOPCOMMAND': 'STOPCOMMAND'})
def StopAutonomousSystemIntent(STOPCOMMAND):
    
    statement("Stopping the autonomous system mode from the script!!")
    
    # to define the message to be sent to the MQTT Broker
    message = "StopAuto"

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    while True:
        microcontroller_response = subscribe(client. topic)

        if microcontroller_response is not None:
            statement (microcontroller_response)
            break

    client.disconnect()

    return None



@ask.intent('ChargingDockIntent', mapping = {'CHARGINGCOMMAND': 'CHARGINGCOMMAND'})
def ChargingDockIntent(CHARGINGCOMMAND):

    # to define the message to be sent to the MQTT Broker
    message = "Go to the charging dock: "

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)
    client.disconnect()

    print("Charging dock Message published....")

    return statement("Going to the charging dock from the script!")



@ask.intent('GoStraightIntent', mapping = {"STRAIGHTCOMMAND": "STRAIGHTCOMMAND"})
def GoStraightIntent(STRAIGHTCOMMAND):
     message = "GoStraight"

     client = connect_mqtt()
     client.loop_start()
     topic = "MQTTCommand/Voice"
     publish(client, topic, message)
     client.disconnect()

     return statement("Going straight from the script!")


@ask.intent("GoLeftIntent", mapping = {"LEFTCOMMAND": "LEFTCOMMAND"})
def GoLeftIntent(LEFTCOMMAND):
    message = "GoLeft"

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    client.disconnect()

    return statement("Going left from the script!")


@ask.intent("GoRightIntent", mapping = {"RIGHTCOMMAND": "RIGHTCOMMAND"})
def GoLeftIntent(RIGHTCOMMAND):
    message = "GoLeft"

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    client.disconnect()

    return statement("Going right from the script!")


@ask.intent("GoReverseIntent", mapping = {"REVERSECOMMAND": "REVERSECOMMAND"})
def GoLeftIntent(REVERSECOMMAND):
    message = "GoReverse"

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    client.disconnect()

    return statement("Going reverse from the script!")



@ask.intent("StopSystemIntent", mapping = {"STOPSYSTEM": "STOPSYSTEM"})
def GoLeftIntent(REVERSECOMMAND):
    message = "Stopping to move: "

    client = connect_mqtt()
    client.loop_start()
    topic = "MQTTCommand/Voice"
    publish(client, topic, message)

    subscribe()

    client.disconnect()

    return statement("Stopping to mowv now from the script!")



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