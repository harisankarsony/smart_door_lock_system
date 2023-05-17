#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

pw2= "Abc@123"

reader = SimpleMFRC522()

# initialize GPIO pins
GPIO.setmode(GPIO.BOARD)
rgpio = 37
GPIO.setup(rgpio,GPIO.OUT)
rgpio_state = 0

# unlock or lock if password matches
while True:
        try:
                id, pw = reader.read()
                pw = pw.strip()
                rgpio_state = GPIO.input(37)
                if rgpio_state:
                        if pw.__eq__(pw2):
                                GPIO.output(rgpio,GPIO.LOW)
                                print("locked by: ", id)
                        else:
                                print("invalid keycard!")
                else:
                        if pw.__eq__(pw2):
                                GPIO.output(rgpio,GPIO.HIGH)
                                print("unlocked by: ", id)
                        else:
                                print("invalid keycard!")
                time.sleep(1)
        finally:
                print()
