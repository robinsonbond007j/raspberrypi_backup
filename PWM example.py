
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.

GPIO.setup(13, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(15, GPIO.OUT)  #motor enable
pwm = GPIO.PWM(13, 100)   # Initialize PWM on pwmPin 100Hz frequency


# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle
while True: # Loop until Ctl C is pressed to stop.
  GPIO.output(15, GPIO.HIGH)    #motor enable
  for dc in range(0, 100, 1):      # Loop from 0 to 100 stepping dc up by 5 each loop
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.05)               # wait for .05 seconds at current LED brightness level
    print(dc)
  for dc in range(100, 0, -1):      # Loop from 95 to 5 stepping dc down by 5 each loop
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.05)               # wait for .05 seconds at current LED brightness level
    print(dc)
 
pwm.stop()
GPIO.cleanup()                     # resets GPIO ports used back to input mode
