import time
import RPi.GPIO as GPIO

btn_pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)


 
while True:
         
    print(GPIO.input(btn_pin))
    time.sleep(1)
        
 
        