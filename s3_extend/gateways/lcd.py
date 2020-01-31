#!/usr/bin/env python

import RPi.GPIO as IO            # calling for header file which helps us use GPIO’s of PI
import time                      # calling for time to provide delays in program
import sys


class LCD:
    """
    This class encapsulates a sonar device with separate
    trigger and echo pins.

    A pulse on the trigger initiates the sonar ping and shortly
    afterwards a sonar pulse is transmitted and the echo pin
    goes high.  The echo pin stays high until a sonar echo is
    received (or the response times-out).  The time between
    the high and low edges indicates the sonar round trip time.
    """

    def __init__(self, pi, trigger, echo):
        """
        The class is instantiated with the Pi to use and the
        gpios connected to the trigger and echo pins.
        """
        IO.setwarnings(False)             # do not show any warnings
        IO.setmode (IO.BCM)               # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)

        IO.setup(6,IO.OUT)                # initialize GPIO Pins as outputs
        IO.setup(22,IO.OUT)
        IO.setup(21,IO.OUT)
        IO.setup(20,IO.OUT)
        IO.setup(16,IO.OUT)
        IO.setup(12,IO.OUT)
        IO.setup(25,IO.OUT)
        IO.setup(24,IO.OUT)
        IO.setup(23,IO.OUT)
        IO.setup(18,IO.OUT)

        while 1:   
            self.send_a_command(0x01);                    # sending 'all clear' command
            self.send_a_command(0x38);                    # 16*2 line LCD
            self.send_a_command(0x0E);                    # screen and cursor ON
            self.send_a_character(0x72);                  # ASCII code for 'H'
            self.send_a_character(0x101);                 # ASCII code for 'E' 
            self.send_a_character(0x108);                 # ASCII code for 'L'
            self.send_a_character(0x108);                 # ASCII code for 'L'
            self.send_a_character(0x111);                 # ASCII code for 'O' 
            self.send_a_character(0x32);                  # ASCII code for ' ' 
            
            # ASCII codes for 'WORLD'
            self.send_a_character(0x119);                    
            self.send_a_character(0x111);
            self.send_a_character(0x114);
            self.send_a_character(0x108);
            self.send_a_character(0x100);
            
            time.sleep(1)

        def send_a_command (command):                    # execute the loop when “sead_a_command” is called
            pin=command
            self.PORT(pin);                              # calling 'PORT' to assign value to data port
            IO.output(6,0)                               # putting 0 in RS to tell LCD we are sending command
            IO.output(22,1)                              # telling LCD to receive command/data at the port by pulling EN pin high
            time.sleep(0.05)
            IO.output(22,0)                              # pulling down EN pin to tell LCD we have sent the data.
            pin=0
            self.PORT(pin);                              # pulling down the port to stop transmitting

        def send_a_character (character):                # execute the loop when “send_a_character” is called
            pin=character
            self.PORT(pin);
            IO.output(6,1)
            IO.output(22,1)
            time.sleep(0.05)
            IO.output(22,0)
            pin=0
            self.PORT(pin);

        def PORT(pin):                                   # assigning PIN by taking PORT value
            if(pin&0x01 == 0x01):
                IO.output(21,1)                          # if  bit0 of 8bit 'pin' is true, pull PIN21 high
            else:
                IO.output(21,0)                          # if  bit0 of 8bit 'pin' is false, pull PIN21 low
            if(pin&0x02 == 0x02):
                IO.output(20,1)                          # if  bit1 of 8bit 'pin' is true, pull PIN20 high
            else:
                IO.output(20,0)                          # if  bit1 of 8bit 'pin' is true, pull PIN20 low
            if(pin&0x04 == 0x04):
                IO.output(16,1)
            else:
                IO.output(16,0)
            if(pin&0x08 == 0x08):
                IO.output(12,1)
            else:
                IO.output(12,0)   
            if(pin&0x10 == 0x10):
                IO.output(25,1)
            else:
                IO.output(25,0)
            if(pin&0x20 == 0x20):
                IO.output(24,1)
            else:
                IO.output(24,0)
            if(pin&0x40 == 0x40):
                IO.output(23,1)                          #pull PIN23 high
            else:
                IO.output(23,0)
            if(pin&0x80 == 0x80):
                IO.output(18,1)                          # if  bit7 of 8bit 'pin' is true pull PIN18 high
            else:
                IO.output(18,0)                          #if  bit7 of 8bit 'pin' is false pull PIN18 low
      

        