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
            if event.value <= 240:
                #print(event.value)
                pwm.ChangeDutyCycle(2)
            if event.value <= 220:
                #print(event.value)
                pwm.ChangeDutyCycle(10)
            if event.value <= 200:
                #print(event.value)
                pwm.ChangeDutyCycle(20)
            if event.value <= 170:
                #print(event.value)
                pwm.ChangeDutyCycle(30)
            if event.value <= 70:
                #print(event.value)
                pwm.ChangeDutyCycle(51)
            if event.value <= 60:
                #print(event.value)
                pwm.ChangeDutyCycle(60)
            if event.value <= 50:
                #print(event.value)
                pwm.ChangeDutyCycle(70)
            if event.value <= 35:
                #print(event.value)
                pwm.ChangeDutyCycle(80)
            if event.value <= 20:
                #print(event.value)
                pwm.ChangeDutyCycle(90)
            if event.value <= 10:
                #print(event.value)
                pwm.ChangeDutyCycle(96)
            
                

    #if deadman switch true then can go backwards
    
    #if event.type == ecodes.EV_ABS:
     #   if event.value >= 160:
            #print(event.value)
       #     pwm.ChangeDutyCycle(0)

    if event.type == ecodes.EV_ABS:
        if event.value == 127:
            #print(event.value)
            pwm.ChangeDutyCycle(40)

    
                

     
