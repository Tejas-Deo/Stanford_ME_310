'''
The sole purpose of this file is to check whether systems are 
communicating with each other.
'''


import paho.mqtt.client as mqtt

print("Waiting to receive messages....")


# Define callback function to handle connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribe to topic when connected
    client.subscribe("AutoSystem/Start")
    client.subscribe("AutoSystem/Stop")
    client.subscribe("AutoSystem/ChargingDock")




# Define callback function to handle incoming messages
def on_message(client, userdata, msg):
    print("Message received from {} with Payload {}".format(msg.topic, msg.payload))





# Define broker information
broker_address = "192.168.10.9"
broker_port = 1883
broker_username = "avatar"
broker_password = "avatar"

# Define client instance
client = mqtt.Client()

# Set username and password for authentication
client.username_pw_set(broker_username, broker_password)

# Set up connection and message callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect(broker_address, broker_port)

# Keep client running to process callbacks
client.loop_forever()
