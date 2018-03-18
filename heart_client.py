import paho.mqtt.client as mqtt
import time
from time import gmtime, strftime

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print(buf)

broker_address="127.0.0.1"
client = mqtt.Client("C1")
client.on_message=on_message
client.on_log=on_log
print("connecting to broker")
client.connect(broker_address)
#client.subscribe("heartbeat")

while True:
    mess = "C1 alive. Time is: " + time.ctime()
    client.publish("heartbeat", mess)
    time.sleep(4)
