#!/usr/bin/env python 
#Autor:Vitor Mazuco 
#Contato:contato@vmzsolutions.com.br 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

while (True):
	GPIO.output(16, True)
	time.sleep(0.5)
	GPIO.output(16, False)
	time.sleep(0.5)
