#!/usr/bin/python3

from sensor.dht_11 import DHT11_Sensor as Sensor 
from handler import FileHandler as Handler
from dotenv import load_dotenv
import os
import logger

def app():
     
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    HUMIDITY_FILE = os.getenv("HUMIDITY_FILE")
    TEMPERATURE_FILE = os.getenv("TEMPERATURE_FILE")

    dht = Sensor()
    data = dht.run()

    temp_file = Handler(HUMIDITY_FILE)
    hum_file = Handler(TEMPERATURE_FILE)

    temp_file.save(data["temperature"])
    hum_file.save(data["humidity"])

if __name__ == "__main__":
	app()
