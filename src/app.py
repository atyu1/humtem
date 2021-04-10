#!/usr/bin/python3

from sensors.humidity_temperature import HumiditySensor as HUMIDITY
from sensors.humidity_temperature import TemperatureSensor as TEMPERATURE
from util.config import ConfigReader

def app():
    config_content = ConfigReader()

    data = []
    sensors = sensor_modularize(config_content)

    for sensor in sensors:
        data.append(sensor.run())


    print (data)
    sender = JsonSender("https://localhost", data)
    sender.login(config_content.tokenuser, config_content.tokenpass)
    sender.push(data)

if __name__ == "__main__":
	app()
