import paho.mqtt.client as mqtt
import machine

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print(buf)

broker_address=""
client = mqtt.Client("F1")
#client.on_message=on_message
client.on_log=on_log

rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

while True:
    print("connecting to broker")
    client.connect(broker_address)
    mess = "F1"
    client.publish("heartbeat", mess)
    client.disconnect()
    time.sleep(10)
    #rtc.alarm(rtc.ALARM0, 10000)
    #machine.deepsleep()

