import paho.mqtt.client as mqtt


broker_address = '192.168.30.2'
broker_port_receive = 9001
broker_port_to_esp = 1883
receive_topic = "UI_receive"   # to receive movement commands from the UI
send_topic = "UI"     # to send movement commands to the microcontroller


# Callback function for when a connection is established
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Websocket topic Connected to MQTT broker!")
    else:
        print("Failed to connect, return code: " + str(rc))

    # Subscribe to the desired topic
    client.subscribe(receive_topic)
    print("Client {} Subscribed to the topic!".format(client))
   


# Callback function for when a message is received
def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode()))
    
    output = msg.payload.decode()

    if output == "straight":
        client.publish(send_topic, "straight")
        print('Straight message published!')

    if output == "left":
        client.publish(send_topic, "left")
        print("Left message published!")

    if output == "right":
        client.publish(send_topic, "right")
        print("Right message published")

    if output == "reverse":
        client.publish(send_topic, "reverse")
        print("Reverse messaged published!")

    if output == "startA":
        client.publish(send_topic, "startA")
        print("Start Auto messaged published!!")

    if output == "stopA":
        client.publish(send_topic, "stopA")

    if output == "CD":
        client.publish(send_topic, "CD")
        print("Charging dock command published....")

    if output == "SM":
        client.publish(send_topic, "SM")
        print("Stop system command published")


# Create a new MQTT client instance
client = mqtt.Client(transport='websockets')

# Set the username and password for the MQTT broker
client.username_pw_set(username="avatar", password="avatar")

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port_receive)    # to receive commands via web sockets

# Start the MQTT client loop to handle network communication and callbacks
client.loop_start()

# Keep the program running to continue receiving messages
while True:
    pass





# # Create a MQTT client instance
# #client = mqtt.Client()

# # Set the MQTT broker to use websockets and specify the port
# #client.ws_set_options(port=9001)

# client = mqtt.Client(transport='websockets')

# # Set the callback functions
# client.on_connect = on_connect
# client.on_message = on_message

# # Connect to the MQTT broker
# client.connect(broker_address, 1883)

# # Start the MQTT loop
# client.loop_forever()



