import paho.mqtt.client as mqtt
import json
import time

# MQTT broker settings
broker = '192.168.30.2'
port = 9001
username = 'avatar'
password = 'avatar'
topic = 'UI_charging'

# List of floating-point values
values = [3.14, 2.718, 1.618, 4.669, 2.302, 1.414, 2.718, 1.618]

# Connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to MQTT broker')
    else:
        print('Connection failed')


# Publish a single value to the topic
def publish_value(value):
    client = mqtt.Client("cd_client", transport='websockets')
    client.on_connect = on_connect

    # Set TLS/SSL options if required
    # client.tls_set()

    # Set username and password if required
    client.username_pw_set(username, password)

    # Connect to the broker
    client.connect(broker, port)

    # Convert the value to JSON
    # payload = json.dumps(value)

    # Publish the JSON payload to the topic
    client.publish(topic, value)
    print("Message published!!")

    # Disconnect from the broker
    client.disconnect()


# Publish the list of values over a period of 2 hours
def publish_values():
    interval = 2 * 3600  # 2 hours in seconds
    num_values = len(values)
    delay = interval / num_values

    for i, value in enumerate(values):
        publish_value(value)
        print(f'Published value {i+1}/{num_values}: {value}')
        time.sleep(delay)

    print('All values published')

# Call the publish_values function
publish_values()
