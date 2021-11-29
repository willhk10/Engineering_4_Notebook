import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
x = 0
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
# Initialize library.




# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Get drawing object to draw on image.


# Draw a black filled box to clear the image.
disp.begin()

# Load default font.

font = ImageFont.load_default()
draw = ImageDraw.Draw(image)

while True:
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    draw.ellipse((x, top + accel_x / 10, x+shape_width, bottom/2 + accel_x / 10), outline=255, fill=0)

    draw.text((x, top+20), "y: " + (str(round(accel_y / 107, 3))), font=font, fill=255)
    draw.text((x, top+40), "z: "  + (str(round(accel_z / 107, 3))), font=font, fill=255)


    disp.image(image)
    disp.display()
    #time.sleep(.5)

# Write two lines of text.



# Display image.

