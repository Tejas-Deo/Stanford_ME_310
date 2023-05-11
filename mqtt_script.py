from paho.mqtt import client as mqtt_client
import sys


# Define broker information
broker_address = '192.168.10.9'
broker_port = 1883
broker_username = "avatar"
broker_password = "avatar"

client_id = "ultrasonic-sensor-subscriber"


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


ultrasonic_sensor_1_topic = "ultrasonic_sensor/sensor_1"
ultrasonic_sensor_2_topic = "ultrasonic_sensor/sensor_2"

client = connect_mqtt()

ultrasonic_sensor_1_output = subscribe(client, ultrasonic_sensor_1_topic)
ultrasonic_sensor_2_output = subscribe(client, ultrasonic_sensor_2_topic)

# print("Output 1: ", ultrasonic_sensor_1_output)
# print("Output 2: ", ultrasonic_sensor_2_output)


# print("Exiting.....")
# sys.exit()

client.loop_forever()





'''
import paho.mqtt.client as mqtt
import subprocess

MQTT_ADDRESS = '192.168.30.2'
MQTT_USER = 'avatar'
MQTT_PASSWORD = 'avatar'
MQTT_TOPIC_1 = 'ultrasonic_sensor/sensor_1'
MQTT_TOPIC_2 = "ultrasonic_sensor/sensor_2"
#MQTT_TOPIC = "outTopic"


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK (Connection Ackownledgement)
      response from the server.
      
    0: Connection accepted
    1: Connection refused, unacceptable protocol version
    2: Connection refused, identifier rejected
    3: Connection refused, server unavailable  
    4: Connection refused, bad user name or password
    5: Connection refused, not authorized

    """

    print('Connected with result code ' + str(rc))

    client.subscribe(MQTT_TOPIC_1)
    client.subscribe(MQTT_TOPIC_2)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    #print(msg.topic + ' ' + str(msg.payload))
    print("Message received from {} with Payload {}".format(msg.topic, msg.payload))



def main():
    # to start the mqtt client
    mqtt_client = mqtt.Client()

    #process = subprocess.Popen(['python', 'alexa_rasp_code.py'], stdout=subprocess.PIPE)

    #print("Process value: ", process)    

    # to set the username and password
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # to connect to the MQTT broker
    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()




if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()
'''