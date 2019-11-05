#RASPBERRY PI BASED PROGRAM TO MEASURE THE DISTANCE TO AN OBJECT USING IR SENSOR

#we need to import the libraries
import RPi.GPIO as GPIO #for raspberry pi gpio support
import time #time for sleep function
import lcd #to display on 16x2 lcd

#connections to lcd gpio pins
D4=5
D5=6
D6=12
D7=13
RS=16
EN=17


#creating mylcd object
mylcd=lcd.lcd()
#initializing lcd pins
mylcd.begin(D4,D5,D6,D7,RS,EN)

#setup gpio modes
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN) #GPIO 2 -> Red LED as output


def detectObject():
    if(GPIO.input(21)==True): #object is far away
            mylcd.clear()
            mylcd.Print("object detected") 
            time.sleep(0.5)
    elif(GPIO.input(21)==False): #object is near
            mylcd.clear()
            mylcd.Print("no object")
            time.sleep(0.5)
            
#set cursor function
def lcdCursor():
    mylcd.blinkCursorOn()
    time.sleep(2)
    mylcd.blinkCursorOff()
    mylcd.clear()


    
#clear GPIOs
def destroy():
    GPIO.cleanup()
    
#main block    
if __name__ == '__main__':
    while True:
        try:
            detectObject()
            lcdCursor()
        
        # If keyboard Interrupt (CTRL-C) is pressed            
        except KeyboardInterrupt:
            destroy()


