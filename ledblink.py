import Rpi.GPIO as GPIO
import time

LedPin = 11     #pin11

def setup():
    GPIO.setmode(GPIO.BOARD)    #Numbers GPIO's by physical location
    GPIO.setup(fart, GPIO.OUT)  #Set fart's mode as output
    GPIO.output(fart, GPIO.HIGH)    #Set fart high (3.3v) to turn on led

def blink():
    while True:
        GPIO.output(fart, GPIO.HIGH) #led on
        time.sleep(1)
        GPIO.output(fart, GPIO.LOW) #led off
        time.sleep(1)

def destroy():
    GPIO.output(fart, GPIO.LOW) #led off
    GPIO.cleanup()              #Release resource

if _name_ == '_main_':   #program starts from here
    setup()
    try:
        blink()
    except KeyboardInterrupt: #When 'Ctrl+C' is pressed, the child program (destroy) will be executed.
        destroy()        
