import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img1.jpg')
img2 = cv.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img2.jpg')
img3 = cv.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img3.jpg')
img4 = cv.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img4.jpg')
img5 = cv.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img5.jpg')

print(img5.shape)

mask = np.full(shape=img5.shape, fill_value=0, dtype=np.uint8)

h, w, c=img5.shape
x=(int)(w/2) - 60; y = (int)(h/2) -60
cv.rectangle(mask, (x,y), (x+120, y+120), (255,255,255), -1)

ress =[]

ress.append(cv.add(img1, img2))
ress.append(cv.addWeighted(img1, 0.5, img2, 0.5, 0)) 
ress.append(cv.subtract(img3, img4))
ress.append(cv.absdiff(img2, img4))
ress.append(cv.bitwise_not(img5))
ress.append(cv.bitwise_and(img5, mask))


titles = []
titles.append('input1')
titles.append('input2')
titles.append('input3')
titles.append('input4')
titles.append('input5')
titles.append('mask')

titles.append('add')
titles.append('addWeighted')
titles.append('subtract')
titles.append('absdiff')
titles.append('bitwise_not')
titles.append('bitwise_and')

images = [img1, img2, img3, img4,img5, mask, ress[0], ress[1],ress[2],ress[3],ress[4],ress[5]]


for i in range(12):
    plt.subplot(2,6,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()




