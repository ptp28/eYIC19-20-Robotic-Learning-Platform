#from gpiozero import LED
#import time

#led = LED(17)
#while(1):
#    led.on()
#    time.sleep(1)
#    led.off();
#    time.sleep(1)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
while(1):
    GPIO.output(17,GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(17,GPIO.LOW)
    #time.sleep(1)