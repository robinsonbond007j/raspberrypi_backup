
from gpiozero import Button, TrafficLights
from signal import pause
from time import sleep
from gpiozero import PWMLED



led = PWMLED(17)
led1 = PWMLED(27)

while True:
    led.value = 1
    led1.value = 0.5
    






