import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

led1, led2, = 21, 26 # Pin each LED is connected to
led1Mode, led2Mode = 1, 0 # Starting state of each LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, False)

while True:
    GPIO.output(led1, led1Mode) #sets the pins as an output
    GPIO.output(led2, led2Mode)
    led1Mode = not led1Mode #changes setting of led1mode from off to on, or vice versa
    led2Mode = not led2Mode #changes setting of led2mode from off to on, or vice versa
    sleep(0.25) #small pause
