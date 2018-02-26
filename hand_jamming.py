import RPi.GPIO as GPIO
import time

green = 11
yellow = 13
red = 15
button = 7

GPIO.setmode(GPIO.BOARD)  #Boradcom chip pin number
GPIO.setup(green, GPIO.OUT)    #Green Light
GPIO.setup(yellow, GPIO.OUT)    #Yellow Light
GPIO.setup(red, GPIO.OUT)    #Red Light
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #Button



print("Here we go! Time to hand jam with sticky hands")

#button == False
    

try:
    while 1:
        if GPIO.input(button):
            GPIO.output(green, GPIO.LOW)
            GPIO.output(yellow, GPIO.LOW)
            GPIO.output(red, GPIO.LOW)
        else:
            GPIO.output(green, GPIO.HIGH)
            
except KeyboardInterrupt: #CTRL+C is pressed, exits program
    GPIO.cleanup() #cleansup IO's
            







