import time
import sys
import json
import configparser
from flask import Flask
from flask import request
from flask_restful import Resource, Api
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt


config = configparser.ConfigParser()
config.read("configuration.ini")

topic = config["DEFAULT"]["topicbase"]


app = Flask(__name__)
api = Api(app)


class RESTbridge(Resource):
    def post(self):
        print("hi")
        pdata = request.form
        print(pdata)
        print(pdata['channel'])
        print(pdata['payload'])
        print(pdata['type'])
        print("lo")
        try:
            topic = config['DEFAULT']['topicbase'] + \
                pdata['type'] + pdata['channel']

            mqttcon = mqtt.Client("RESTbridge")
            mqttcon.username_pw_set(
                config['DEFAULT']["mqtt_user"],
                config['DEFAULT']["mqtt_pass"]
            )
            mqttcon.connect(config['DEFAULT']["mqtt_server"],
                            int(config['DEFAULT']["mqtt_port"]),
                            int(config['DEFAULT']["mqtt_conntimeout"])
                            )
            mqttcon.publish(topic, pdata['payload'])
            mqttcon.disconnect()

            print("{} Sent => CHANNEL: {} PAYLOAD: {}".format(time.strftime(
                "%d/%b/%y %H:%M:%S", time.localtime()),
                topic, pdata['payload']))
            return {'status': 'success'}
        except Exception as inst:
            print("Error: " + inst)


api.add_resource(RESTbridge, '/RESTbridge')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(
        config["DEFAULT"]['flask_port']))
