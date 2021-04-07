import paho.mqtt.client as mqtt
import logging
import time

sub_to = "farms/+/aggregators/+/sensors/+/data"
pub_to = "farms/1/aggregators/1/sensors/1/commands"
# sub_to = "aggregators/1/sensors/+/data"
# pub_to = "aggregators/1/sensors/1/commands"

client = mqtt.Client("test_collector")
logger = logging.getLogger("test_collector")
logging.basicConfig(level=logging.DEBUG)

def on_message(client, userdata, msg):
    msg = msg.payload.decode('utf-8')
    logger.info(f"Message received : \"{msg}\"")

client.on_message = on_message
logger.info("Trying to connect to broker...")
client.connect("127.0.0.1", port=1880)
logger.info("Connected to broker")
client.loop_start()
logger.info(f"Subscribing to topic {sub_to}")
client.subscribe(sub_to)

for i in range(0, 10):
    logger.info(f"publishing to topic {pub_to}")
    client.publish(pub_to, "example command from backend")
    time.sleep(3)

client.disconnect()
client.loop_stop()
