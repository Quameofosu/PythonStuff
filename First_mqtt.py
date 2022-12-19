import paho.mqtt.client as mqtt

# Set up the MQTT client
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# Publish a message with the topic "bike/sensor/accelerometer"
client.publish("bike/sensor/accelerometer", "Accelerometer data")



while True:
    text = input("PLease enter a text between 1 and 6: ")
    if text.isdigit() and 1 <= int(text) <= 6:
        # This text is a valid number between 1 and 6
        break
    else:
        #The text is not a valid number between 1 and 6
        print("Invalid input. Please try again.")
