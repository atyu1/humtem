#!/usr/bin/python3

from sensors.dht11 import Dht11_Sensor as Sensor 
from dotenv import load_dotenv
import os
import logger

def app():
     
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    data = []

    Sensor()
    data.append(Sensor.run())

    sender = JsonSender("https://localhost", data)
    sender.login(config_content.tokenuser, config_content.tokenpass)
    sender.push(data)

if __name__ == "__main__":
	app()
