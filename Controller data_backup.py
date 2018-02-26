#import evdev
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO # Import GPIO Lib
import time #import time lib

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
#print(gamepad)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
pwm = GPIO.PWM(36, 100)

#button variables
ready = 304
cruise_con = 308
coast = 16
deadman = False
backwards = 250

dc=0
pwm.start(dc)



#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #print(categorize(event))
    
    

   
    

    #if deadman switch true then can go foward
    
    if event.type == ecodes.EV_ABS:
        if event.value >= 2:
            if event.value <= 80:
                #print(event.value)
                pwm.ChangeDutyCycle(25)
            if event.value <= 60:
                #print(event.value)
                pwm.ChangeDutyCycle(50)
            if event.value <= 30:
                #print(event.value)
                pwm.ChangeDutyCycle(75)
            if event.value <= 10:
                #print(event.value)
                pwm.ChangeDutyCycle(90)
            
                

    #if deadman switch true then can go backwards
    
    if event.type == ecodes.EV_ABS:
        if event.value >= 160:
            #print(event.value)
            pwm.ChangeDutyCycle(0)

    
                

     
