#SIMPLE RASPBERRY PI PROGRAM TO TEST ANY GPIO ON LED ARRAY 
#import GPIO library to use GPIO pins 
import RPi.GPIO as GPIO

#set gpio pin mode
GPIO.setmode(GPIO.BCM)

#set that pin as output
GPIO.setup(21, GPIO.OUT)

#set that pin as True or HIGH 
GPIO.output(21, True)
