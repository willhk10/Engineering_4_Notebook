import time
import picamera
import os

stopmotion_pin = 16

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(stopmotion_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

channel = GPIO.wait_for_edge(stopmotion_pin, GPIO.FALLING, bouncetime=200)


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
		if GPI.input(stopmotion_pin) == False
			# Camera warm-up time
			time.sleep(1)
			counter += 1
    			camera.capture(f'../Pictures/{name}/image{counter}.jpg')

