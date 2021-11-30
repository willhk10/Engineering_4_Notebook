from picamera import PiCamera

from time import sleep

camera = PiCamera()
camera.start_preview(alpha=192)
sleep(1)
camera.capture("/home/pi/Documents/Engineering_4_Notebook/Pictures/pic.jpg")
camera.stop_preview()
