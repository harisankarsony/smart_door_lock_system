#!/usr/bin/env python

import RPi.GPIO as GPIO
import BlynkLib

BLYNK_AUTH = '5MYYj4m6F7C1ZN3DEQ5qrBiZ92PEWqV2'

GPIO.setmode(GPIO.BCM)
rgpio=26
GPIO.setup(rgpio,GPIO.OUT)

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#sync virtual pin with server
@blynk.on("connected")
def blynk_connected():
    blynk.sync_virtual(0)

# Register virtual pin handler
@blynk.on("V0")
def v0_write_handler(value):
    if int(value[0]) == 1:
        GPIO.output(rgpio,GPIO.HIGH)
        print("unlocked")
    else:
        GPIO.output(rgpio,GPIO.LOW)
        print("locked")

while True:
    blynk.run()
