from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(25)
camera = PiCamera()

while True:
#    filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
	filename =(f"{datetime.now()}.h264")
#	print(datetime.now())
	pir.wait_for_motion()
	print("motion detected")
	camera.start_recording(filename)
#	print("3rd")
	pir.wait_for_no_motion()
	print("No motion, waitin.")
	camera.stop_recording()

#while True:
#	if pir.motion_detected:
#		print("motion")
	
#	else:
#		print("what")

#	if not pir.motion_detected:
#		print("no motion")
