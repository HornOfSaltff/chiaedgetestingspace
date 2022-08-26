#!/usr/bin/python3

import os
import subprocess
import libcam_image

# Get date and separate day and time
date = subprocess.getoutput("date +%F")
time = subprocess.getoutput("date +%H:%M")

print("Start libcamera")
# Take picture
out = os.system("libcamera-hello")
#out = os.system("libcamera-jpeg -o test.jpg")
#out = os.system("libcamera-still -o "+date+"/"+time+".jpg -n")
print("End libcamera")