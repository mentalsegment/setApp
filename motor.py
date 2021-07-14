import RPi.GPIO as GPIO
import time


in1 = 16
in2 =12
en = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en,1000)

p.start(100)
time.sleep(1)
p.stop()
