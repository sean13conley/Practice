# make an image with random pixels use open cv and numpy
# try an make an image that's 100x100 pixels with random colors

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy

img = mpimg.imread('stinkbug.png')

print(img)

imgplot = plt.imshow(img)
plt.show()


img2 = cv2.imread('ender_sword.png')

#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img2)

img2plot = plt.imshow(img2)

plt.show()
# plt.imshow(img)
# plt.show()

