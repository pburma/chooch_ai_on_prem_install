from chooch_mqtt import mqtt_object
import base64
import json


data_json = "{\"testpat\":\"datapat1111\"}"
my_mqtt_object = mqtt_object()
my_mqtt_object.send_message(data_json)

