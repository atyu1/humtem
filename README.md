# HumTem

## Overview
Humidity and Temperature reader from Raspberry PI via DHT11 sensor.
We are using it to read the temperature and Humidity and communicate via chat bot to provide actual status.

Idea:
 - We will provide the current values via chat bot if we ask
 - We will provide the current values regularly like every 1h

## Hardware
 Used HW:
 - Raspberry PI 4
 - Sensor DHT 11

 Cabling for sensor:
 - ToDo

## Dependencies
 - DHT 11 Module https://github.com/szazo/DHT11_Python
 - Docker containers to offload installation: https://stackoverflow.com/questions/30059784/docker-access-to-raspberry-pi-gpio-pins

## Code insights
 - Sensor is using abstract class Sensor
 - All sensors must implement function run() 
