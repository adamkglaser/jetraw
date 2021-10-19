import hardware.pco as pco
import numpy
import jetraw

cam = pco.Camera(camera_number = 2)
print(cam)

cam.configuration = {'exposure time': 10e-3,
             'trigger': 'auto sequence',
             'acquire': 'auto',
             'pixel rate': 272250000,
             'binning': (1, 1)}

cam.record(number_of_images = 10, mode = 'sequence non blocking')

nFrames = 10
imgs = numpy.zeros((nFrames, 2048, 2060), dtype = 'uint16')

num_acquired = 0

cam.start(mode = 'sequence non blocking')

while num_acquired < nFrames:
	print(num_acquired)
	cam.wait_for_next_image(num_acquired)
	imgs[num_acquired] = cam.image(num_acquired)[0]
	num_acquired += 1

cam.close()

jetraw.imwrite('temp.tif', imgs[0], description="Python Jetraw Tests")