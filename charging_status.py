import paho.mqtt.client as mqtt


broker_address = '192.168.30.2'
broker_port = 9001
receive_topic_from_microncontroller = "charging_status"
send_topic_to_UI = "UI_charging"


# Callback function for when a connection is established
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
    else:
        print("Failed to connect, return code: " + str(rc))

    # Subscribe to the desired topic
    client.subscribe(receive_topic_from_microncontroller)
    print("Subscribed to the topic!")


# Callback function for when a message is received
def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode()))
    
    output = msg.payload.decode()

    client.publish(send_topic_to_UI, output)
    print("Message published")


# Create a new MQTT client instance
client = mqtt.Client('cg_client', transport='websockets')

# Set the username and password for the MQTT broker
client.username_pw_set(username="avatar", password="avatar")

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT client loop to handle network communication and callbacks
client.loop_start()

# Keep the program running to continue receiving messages
while True:
    pass