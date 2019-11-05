#switch program to use a switch to be tested on a led or buzzer
import RPi.GPIO as GPIO
import time

#SETUP OF GPIO MODE AS BCM
GPIO.setmode(GPIO.BCM)

#SETUP OF GPIO AS INPUT N OUPUT
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(18, GPIO.OUT)  #LED to GPIO24

#USING A SIMPLE EXCEPTION HANDLING
try:
    while True:
         button_state = GPIO.input(20)
         if button_state == False:
             GPIO.output(18, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(18, False)
except:
    GPIO.cleanup()
