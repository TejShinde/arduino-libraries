#RASPBERRY PI PROGRAM TO USE LDR WITHOUT ADC IC

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

#set 21 as the pin to use as the LDR input
pin_to_circuit = 21;

#rc_time function to count the time LDR is low
def rc_time (pin_to_circuit): 
	count = 0 
	GPIO.setup(pin_to_circuit, GPIO.OUT) 
	GPIO.output(pin_to_circuit, GPIO.LOW) 
	time.sleep(0.1) 
	GPIO.setup(pin_to_circuit, GPIO.IN) 
	while (GPIO.input(pin_to_circuit) == GPIO.LOW): 	
		count += 1 
	return count 

#main block    
if __name__ == '__main__':
	try: 
		while True: 
			print(rc_time(pin_to_circuit)) 
        # If keyboard Interrupt (CTRL-C) is pressed            
	except KeyboardInterrupt: 
		GPIO.cleanup()

