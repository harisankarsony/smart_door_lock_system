#!/usr/bin/env python

import firebase_admin
import BlynkLib
from gpiozero import Button
from time import sleep
from firebase_admin import messaging
from firebase_admin import credentials
from threading import Thread

value2 = ""
BLYNK_AUTH = '5MYYj4m6F7C1ZN3DEQ5qrBiZ92PEWqV2'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected():
    # to sync a specific virtual pin
    blynk.sync_virtual(2)
    
# Register virtual pin handler
@blynk.on("V2")
def v2_write_handler(value):
    global value2
    value2 = value2.join(value)

# load service account cedentials file
cred = credentials.Certificate("/home/h4r1/Desktop/doorlockapp-6b97f-firebase-adminsdk-tfsa5-1b1daeb703.json")
firebase_admin.initialize_app(cred)

def send_to_token():
    global value2
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    message = messaging.Message(
    data={
        'title': 'Doorbell Alert!',
        'body': 'You have a visitor. Tap to open app.',
    },token=value2,)
  
    # Send a message to the device corresponding to the provided
    # registration token.
    print("Firebase token: ", value2)
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]

# thread to run blynk sync in parallel
def blynksync():
    while True:
        blynk.run()

t1 = Thread(target = blynksync)
t1.start()

# send notification on button press
button = Button(16)
while True:
    button.wait_for_press()
    send_to_token()
    sleep(2)
