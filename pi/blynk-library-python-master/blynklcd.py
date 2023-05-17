#!/usr/bin/env python

import drivers
import BlynkLib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
rgpio = 26
GPIO.setup(rgpio,GPIO.OUT)
rgpio_state = 0

BLYNK_AUTH = '5MYYj4m6F7C1ZN3DEQ5qrBiZ92PEWqV2'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Load the driver and set it to "display"
display = drivers.Lcd()
def long_string(display, text='', num_line=1, num_cols=16):
		# Parameters: (driver, string to print, number of line to print, number of columns of your display)
		
		if len(text) > num_cols:
			display.lcd_display_string(text[:num_cols], num_line)
			display.lcd_display_string(text[num_cols:], num_line+1)
			
		else:
			display.lcd_display_string(text, num_line)

#sync virtual pin with server
@blynk.on("connected")
def blynk_connected():
    blynk.sync_virtual(1)

# Register virtual pin handler
@blynk.on("V1")
def v1_write_handler(value):
	value2 = ""
	value2 = value2.join(value)
	print(value2)
	display.lcd_clear()
	long_string(display, value2, 1)

# loop blynk v1 update
while True:
	blynk.run()
	temp = rgpio_state
	# loop gpio state change
	while True:
		rgpio_state = GPIO.input(26)
		if temp != rgpio_state:
			if rgpio_state:
				display.lcd_clear()
				long_string(display,"Unlocked", 1)
				print("Unlocked")
			else:
				display.lcd_clear()
				long_string(display,"Locked", 1)
				print("Locked")
			# sync back to v1 value
			time.sleep(1.5)
			display.lcd_clear()
			blynk.sync_virtual(1)
		break
