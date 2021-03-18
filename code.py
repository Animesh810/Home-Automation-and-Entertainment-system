import os
from time import sleep
import RPi.GPIO as GPIO
from camerafunc import *
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
motion_sense = 37 # gpio26 #pulled down
lock_gate = 7 # gpio17
late_light = 5

GPIO.cleanup()
#motionsensor interrupt
GPIO.setup(motion_sense, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#lock controller
GPIO.setup(lock_gate, GPIO.OUT)
GPIO.output(lock_gate, GPIO.HIGH)
GPIO.setup(late_light, GPIO.OUT)
GPIO.output(late_light, GPIO.HIGH)
#it works done change it
songs = [ 'Ipl.mp3', 'waka_waka.mp3' ]
SONG_COMMAND_B = 'omxplayer '
SONG_COMMAND_E = ' &'

while True:
    GPIO.output(lock_gate, GPIO.HIGH) 
    GPIO.output(late_light, GPIO.HIGH) 
    
    if(GPIO.input(motion_sense)):
        #camera input required
            
        known = cam_trig()
        #known = True
        
        if(known):
            GPIO.output(lock_gate, GPIO.LOW) 
            sleep(3)
            GPIO.output(lock_gate, GPIO.HIGH)
            sleep(3)
            temp = SONG_COMMAND_B + random.choice(songs) + SONG_COMMAND_E
            GPIO.output(late_light, GPIO.LOW) 
            os.system(temp)
            sleep(30)
        else:
            sleep(10)
            #sleep(1)
    
        #sleep(10)
    
    
