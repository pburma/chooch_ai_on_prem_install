import paho.mqtt.client as mqtt
import base64
import json

class mqtt_object(object):
    def __init__(self):
       self.mqtt_enabled = False
       print("try mqtt")
       try:
            with open("config.json") as f:
                json_data = json.load(f)
                print(json_data["mqtt_info"])

            self.mqtt_info = json_data["mqtt_info"]
            # self.mqtt_info = {"broker_password": "","publish_url": "/chooch/s1","broker_username": "", "enable_tls": False, "broker_url": "public.vantiq.com", "broker_port": "1883"}


            print(self.mqtt_info["broker_url"])

            if len(str(self.mqtt_info["broker_url"])) > 5:
                self.client = mqtt.Client(protocol=mqtt.MQTTv31)


                self.client.username_pw_set(self.mqtt_info["broker_username"], str(base64.b64decode(str(self.mqtt_info["broker_password"]).replace("b'", "").replace("'", ""))).replace("b'", "").replace("'", ""))


                rc = self.client.connect(self.mqtt_info["broker_url"], int(self.mqtt_info["broker_port"]), 60)

                print("connect() return code:", rc)

                if rc == 0:
                    self.mqtt_enabled = True


       except:
               print("no mqtt")

    def is_mqtt_enabled(self):

        return  self.mqtt_enabled


    def send_message(self, json_data):

        if  self.mqtt_enabled == True:

            self.client.publish(self.mqtt_info["publish_url"], json_data)