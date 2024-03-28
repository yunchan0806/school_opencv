import cv2 as cv

import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('WIN_20240313_01_03_18_Pro.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, sheck with os.path.existe()"

ret, thresh1 = cv.threshold(img, 127,255,cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)
ret, thresh4 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)

titles = ['original image', 'binary', 'binary_inv','trunc','tozero', 'tozero_inv']

images = [img, thresh1, thresh2, thresh3, thresh4, thresh]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray', vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()