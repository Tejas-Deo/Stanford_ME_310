import paho.mqtt.client as mqtt

MQTT_ADDRESS = '192.168.10.14'
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