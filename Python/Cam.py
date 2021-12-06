import picamera

from time import sleep


with picamera.Picamera() as camera:
	camera.resolution = (1024,768)
	camera.start_preview(alpha=192)
	sleep(1)
	camera.capture("/home/pi/Documents/Engineering_4_Notebook/Pictures/camera_test.jpg")
	print("running")

