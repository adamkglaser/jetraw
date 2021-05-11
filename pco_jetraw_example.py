# -*- coding: utf-8 -*-

import pco
import jetraw
import time

nFrames = 10

# cam = pco.Camera(camera_number = 2)
# print(cam)

# cam.record(nFrames, 'multitif', file_path='C:/temp/recorder/img')

# time.sleep(10)

# cam.close()

cam = pco.Camera(camera_number = 2)
cam.configuration = {'pixel rate': 272250000}
print(cam.configuration)

cam.record(nFrames, 'sequence dpcore')

time.sleep(10)

images, metas = cam.images()

with jetraw.TiffWriter('C:/temp/recorder/img_jetraw.tif', description='PCO and Jetraw!') as tif:
    for frame in images:
        tif.write(frame)

cam.close()