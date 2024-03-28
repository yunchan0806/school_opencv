import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('')
img2 = cv.imread('')
img3 = cv.add()

img4 = cv.addWeighted(img1, 0.5, img2, 0.5, 0)

titles =['src', 'map','add','addweighht']
imgs = [img1,img2,img3,img4]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()