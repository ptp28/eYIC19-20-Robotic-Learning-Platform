"""

                    * Project Name: 	e-Yantra Project
                    * Author List: 		Akash Rasal, e-Yantra Team
                    * Filename: 		rpi_import.py
                    * Functions: 		readUltrasonic(GPIO_TRIGGER , GPIO_ECHO), readSound(gpioPIN), readPIR(gpioPIN), readFire(gpioPIN),
                                        readPhototransistor(gpioPIN), readTemp(gpioPIN), writeServo(pinNO,Degree), toggleLED(pinNO,state),
                                        toggleLED(pinNO,state), toggleBuzzer(pinNO,state), toggleBuzzer(pinNO,state)
                    * Global Variables:	NONE
"""

import RPi.GPIO as GPIO
import time                             # calling for time to provide delays in program
import Adafruit_DHT

#ultrasonic sensor
 """
                    * Function Name:	readUltrasonic()
                    * Input:		    GPIO_TRIGGER -> GPIO trigger listens for pin state change and then perform some action, 
                                        GPIO_ECHO -> gives output according to the pin state change.
                    * Output:		    distance is calculated.
                    * Logic:		    after setting the GPIO direction and trigger, calculate time difference trigger pin and echo pin.
                                        Find the distance : distance = (TimeElapsed * 34300) / 2  
                    * Example Call:		readUltrasonic(GPIO_TRIGGER , GPIO_ECHO)
                    
"""

def readUltrasonic(GPIO_TRIGGER , GPIO_ECHO):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
   
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2 
    return distance


#sound detection sensor
"""
                    * Function Name:	readSound()
                    * Input:		    gpioPIN -> takes the gpio pin number from the user. 
                                        
                    * Output:		    sound is detected.
                    * Logic:		    When the input pin detects a 'high', sound is detected.
                    * Example Call:		readSound(9)
                    
"""

def readSound(gpioPIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioPIN, GPIO.IN) #PIR
    
    try:
        time.sleep(2) # to stabilize sensor
        for i in range(100):
            if GPIO.input(gpioPIN):
                GPIO.cleanup()
                return True
            time.sleep(0.1) #loop delay, should be less than detection delay
    except:
        GPIO.cleanup()
        return False

#pir sensor
"""
                    * Function Name:	readPIR()
                    * Input:		    gpioPIN -> takes the gpio pin number from the user.  
                    * Output:		    detection of moving living objects.
                    * Logic:		    initially set the gpio pin number and Broadcom SOC number then stabilize the sensor by putting it to 
                                        sleep mode
                    * Example Call:		readPIR(5)
"""
def readPIR(gpioPIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioPIN, GPIO.IN) #PIR
    
    try:
        time.sleep(2) # to stabilize sensor
        for i in range(100):
            if GPIO.input(gpioPIN):
                GPIO.cleanup()
                return True
            time.sleep(0.1) #loop delay, should be less than detection delay

    except:
        GPIO.cleanup()
        return False

#fire sensor
"""
                    * Function Name:	readFire()
                    * Input:		    gpioPIN -> takes the gpio pin number from the user.  
                    * Output:		    used for fire detection
                    * Logic:		    when the input pin detects 'high' then fire is detected. 
                    * Example Call:		readPIR(10)
"""

def readFire(gpioPIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    Flamein = gpioPIN
    #Switch Pin
    GPIO.setup(Flamein, GPIO.IN)
    if (GPIO.input(25) == True):
        GPIO.cleanup()
        return True;
    GPIO.cleanup()    
    return False;

#phototransistor
"""
                    * Function Name:	readPhototransistor()
                    * Input:		    gpioPIN -> takes the gpio pin number from the user.  
                    * Output:		    used for detecting obstacle 
                    * Logic:		    create a loop to catch a change in the digital output, check if GPIO pin number=0
                    * Example Call:		readPhototransistor(11)
"""

def readPhototransistor(gpioPIN):
    GPIO.setmode(GPIO.BCM) # use board pin numbers
    pin = gpioPIN
    GPIO.setup(pin, GPIO.IN) 

    #create a loop to catch a change in the digital output
    if(GPIO.input(pin) == 0):
        GPIO.cleanup()
        return False
    else:
        GPIO.cleanup()
        return True

#temp sensor
"""
                    * Function Name:	readTemp()
                    * Input:		    gpioPIN -> takes the gpio pin number from the user.  
                    * Output:		    used to read the temperature  
                    * Logic:		    
                    * Example Call:		readTemp(12)
"""
def readTemp(gpioPIN):
    sensor = Adafruit_DHT.DHT11
    gpio = gpioPIN
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
          GPIO.cleanup()
          return    temperature, humidity;
    else:
        GPIO.cleanup()
        return 0,0;

#write servo
"""
                    * Function Name:	writeServo()
                    * Input:		    pinNo  -> takes the gpio pin number from the user.
                                        Degree -> the degree of rotation of the motor.    
                    * Output:		    used for detecting obstacle. 
                    * Logic:		    programming the GPIO by BCM pin numbers. initialize GPIO19 as an output. 
                                        GPIO19 as PWM output, with 50Hz frequency.
                                        generate PWM signal with 7.5% duty cycle.
                    * Example Call:		writeServo(15)
"""
def writeServo(pinNO,Degree):
    GPIO.setmode (IO.BCM)            
    GPIO.setup(pinNO,IO.OUT)             
    p = GPIO.PWM(pinNO,50)              
    p.start(7.5)                            
    p.ChangeDutyCycle(Degree)
    GPIO.cleanup()                   

#toggle LED
"""
                    * Function Name:	toggleLED()
                    * Input:		    pinNo  -> takes the pin number from the user.
                                        state ->  checks wheather led is on or off
                    * Output:		    checks wheather led is glowing
                    * Logic:		    
                    * Example Call:		toggleLED(17)
"""
def toggleLED(pinNO,state):
    GPIO.setmode(GPIO.BCM)
    LED = pinNO
    ledState = state
    GPIO.setup(LED,GPIO.OUT)
    GPIO.output(LED, ledState)
    GPIO.cleanup()

# def toggleLED(pinNO,state):
#     GPIO.setmode(GPIO.BCM)
#     LED = pinNO
#     if(state == 0):
#         ledState = False
#         GPIO.setup(LED,GPIO.OUT)
#         GPIO.output(LED, ledState)
#     elif(state == 1):
#         ledState = True
#         GPIO.setup(LED,GPIO.OUT)
#         GPIO.output(LED, ledState)
#     GPIO.cleanup()    

#toggle Buzzer
"""
                    * Function Name:	toggleBuzzer()
                    * Input:		    pinNo  -> takes the pin number from the user.
                                        state ->  checks wheather buzzer is on or off.
                    * Output:		    checks wheather the buzzer is on or off.
                    * Logic:		    
                    * Example Call:		toggleBuzzer(18)
"""
def toggleBuzzer(pinNO,state):
    GPIO.setmode(GPIO.BCM)
    Buzzer = pinNO
    buzzState = state
    GPIO.setup(Buzzer,GPIO.OUT)
    GPIO.output(Buzzer, buzzState)
    GPIO.cleanup()

# def toggleBuzzer(pinNO,state):
#     GPIO.setmode(GPIO.BCM)
#     Buzzer = pinNO
#     if(state == 0):
#         buzzState = False
#         GPIO.setup(Buzzer,GPIO.OUT)
#         GPIO.output(Buzzer, buzztate)
#     elif(state == 1):
#         buzzState = True
#         GPIO.setup(Buzzer,GPIO.OUT)
#         GPIO.output(Buzzer, buzzState)
#     GPIO.cleanup()
