import time
import picamera
import RPi.GPIO as GPIO
import os

stopmotion_pin = 16
print("1")
GPIO.setwarnings(False)
print("2")
GPIO.setmode(GPIO.BCM)
print("3")
GPIO.setup(stopmotion_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
print("4")
#channel = GPIO.wait_for_edge(stopmotion_pin, GPIO.FALLING, bouncetime=200)
print("5")
counter = 0
name = input("Enter project name")
os.mkdir(f"../Pictures/{name}")

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	while True:
	#if channel is none:
	#GPIO.input(stopmotion_pin)
	#else:
		if GPIO.input(stopmotion_pin) == False:
			# Camera warm-up time
			time.sleep(1)
			counter += 1
			print(counter)
			camera.capture(f'../Pictures/{name}/image{counter}.jpg')
