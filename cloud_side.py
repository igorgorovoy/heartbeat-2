import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print(buf)

broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("P1")
client.on_message=on_message
client.on_log=on_log
print("connecting to broker")
client.connect(broker_address)
print("Subscribing to topic","heartbeat")
client.subscribe("heartbeat")
print("Publishing message to topic","heartbeat")
client.publish("heartbeat","I'm listening cloud-side")
client.loop_forever()
while True:
    print("Test")
    time.sleep(3)
