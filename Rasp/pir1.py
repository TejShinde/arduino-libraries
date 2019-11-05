#RASPBERRY PI CODE TO ALERT ON INTRUDER DETECTION USING PIR SENSOR

#Libraries to import
import RPi.GPIO as GPIO #for gpio on raspberry pi
import time #for sleep function
import lcd #to display on 16x2 lcd

#setup gpio pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(20, GPIO.OUT)         #LED/buzzer output pin

#lcd connections to GPIO pins
D4=5 
D5=6
D6=12
D7=13
RS=16
EN=17

#create mylcd object
mylcd=lcd.lcd()
#initilize lcd inputs
mylcd.begin(D4,D5,D6,D7,RS,EN)

def pirSensor():
    i = GPIO.input(21)
    if i == 0:                 #When output from motion sensor is LOW
        print("No intruders")
        GPIO.output(20, 0)  #Turn OFF LED/buzzer
        mylcd.clear()
        mylcd.Print("No intruders") 
        time.sleep(0.5)

    else:               #When output from motion sensor is HIGH
        print("Intruder detected")
        mylcd.clear()
        mylcd.Print("Intruder detected")
        GPIO.output(20, 1)  #Turn OFF LED/buzzer         
        time.sleep(0.5)

#clear GPIOs
def destroy():
    GPIO.cleanup()
    
time.sleep(5)
while True:
    try:
        pirSensor()
    except KeyboardInterrupt:
        destroy()    