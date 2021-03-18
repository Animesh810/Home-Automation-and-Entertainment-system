#bad mai dekhenge
import os
from time import sleep
from PIL import Image
import psutil
#import blue 

#TIMEOUT = 5

def cam_trig():
    
    # uses Fswebcam to take picture    
    os.system('fswebcam -r 720x720 -q --save /home/pi/lol/temp.jpg')
    #img =
    #return True
    img = Image.open("temp.jpg")
    img.show()
    #img.save("/images/example.jpg")
    sleep(10)
    # hide image
    
    for proc in psutil.process_iter():
        if proc.name() == "display":
           proc.kill()
    
    #val = blue_trigger()
    val = input("Let this Person in? ")
    #val = 'y'
    
    if val == 'y' :
        return True
    
    else :
        return False
    
    