#!/usr/bin/env python
# encoding: utf-8


import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
from time import sleep

COMMASPACE = ', '

def SendEMail():
    sender = ''
    gmail_password = ''
    recipients = ['']
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Soil is about to dry and water will be poured'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

   

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

GPIO.setup(23, GPIO.OUT)


GPIO.output(23, GPIO.HIGH)



while (True):
    
    if GPIO.input(17):
        print("Need to Water The Garden and Water Pump will be Switched On")
        SendEMail()
        GPIO.output(23, GPIO.LOW)
        while (True):
            if not GPIO.input(17):
                GPIO.output(23, GPIO.HIGH)
                break
    else:
        print("Soil has enough Moisture")



        

