#!/usr/bin/env python

import RPi.GPIO as GPIO
from gpiozero import Button
import time

# initialize GPIO pins
GPIO.setmode(GPIO.BCM)
rgpio = 26
GPIO.setup(rgpio,GPIO.OUT)
rgpio_state = 0
button = Button(24)

# unlock or lock on button press
while True:
	button.wait_for_press()
	rgpio_state = GPIO.input(26)
	if rgpio_state:
			GPIO.output(rgpio,GPIO.LOW)
			print("locked")
	else:
		GPIO.output(rgpio,GPIO.HIGH)
		print("unlocked")
	time.sleep(0.5)
