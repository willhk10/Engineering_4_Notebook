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
    GPIO.output(led1, led1Mode)
    GPIO.output(led2, led2Mode)
    led1Mode = not led1Mode
    led2Mode = not led2Mode
    sleep(0.25)
