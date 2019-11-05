#RASPBERRY PI BASED PROGRAM TO CONTROL MOTOR DRIVER USING PWM

import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep  # Importing sleep from time library

EN1 = 25           # Initializing the GPIO pin 25 for the enable 1 
IN1 = 26           # Initializing the GPIO pin 26 for input 1 of the motor driver
IN2 = 27           # Initializing the GPIO pin 27 for input 2 of the motor driver   

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering

GPIO.setup(EN1,GPIO.OUT)        ## Declaring as EN1 output pin
GPIO.setup(IN1,GPIO.OUT)        ## Declaring as IN1 output pin
GPIO.setup(IN2, GPIO.OUT)       ## Declaring as IN2 output pin

pwm = GPIO.PWM(EN1, 100)    # Created a PWM object
pwm.start(0)                    # Started PWM at 0% duty cycle

    
#clear GPIOs
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':     # Program start from here
    try:
        while 1:                    # Loop will run forever
            for x in range(100):    # This Loop will run 100 times
                pwm.ChangeDutyCycle(x) # Change duty cycle
                GPIO.output(26, True)
                GPIO.output(27, False)
                    
    # If keyboard Interrupt (CTRL-C) is pressed
    except KeyboardInterrupt:
        pass        # Go to next line
    
        pwm.stop()      # Stop the PWM
    destroy()

    
    
    
        