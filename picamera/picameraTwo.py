#!/usr/bin/python3
# import libcamera
# #libcamera.ColorSpace.Sycc = libcamera.ColorSpace.Jpeg
# import picamera2 as Picamera2

#Above is a work around to get picamera to work. If libcamera or picamera2 is 
#updated this will also need to be updated.

# import time

# picam2 = Picamera2()
# picam2.start()
# time.sleep(2)

# fname = (time.strftime("%y-%b-%d_%H:%M"))
# variable = fname + ".jpg"
# picam2.capture_file(variable)
# #picam2.capture_file("test.jpg")


import time
import libcamera
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()
time.sleep(2)

fname = (time.strftime("%y-%b-%d_%H:%M"))
variable = fname + ".jpg"
# picam2.capture_file(variable)
# #picam2.capture_file("test.jpg")
metadata = picam2.capture_file(variable)
print(metadata)

picam2.close()


# from picamera2 import Picamera2
# picam2 = Picamera2()
# picam2.start_and_capture_file("test.jpg")