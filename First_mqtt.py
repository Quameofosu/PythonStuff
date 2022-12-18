import paho.mqtt.client as mqtt

# Set up the MQTT client
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# Publish a message with the topic "bike/sensor/accelerometer"
client.publish("bike/sensor/accelerometer", "Accelerometer data")


