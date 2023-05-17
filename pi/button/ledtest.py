from gpiozero import LED, Button
from time import sleep

led = LED(16)
button = Button(24)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)
