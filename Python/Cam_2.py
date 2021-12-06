import time
import picamera
effects = ['negative', 'solarize', 'sketch', 'denoise', 'emboss']

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768)
  camera.start_preview()
  # Camera warm-up time
  time.sleep(1)
  for effect in effects: 
    camera.image_effect = effect       
    camera.capture(f'../Pictures/picturewith{effect}.jpg')
  
      
