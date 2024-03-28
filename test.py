import numpy as np
import cv2
from matplotlib import pyplot as plt
def nothing():
    pass
cam = cv2.VideoCapture(0)

cv2.namedWindow("rgb track bar")
if cam.isOpened() == False:
    print('Cannot open the camera-%d' % (0))
    exit()

cv2.createTrackbar("red color", "rgb track bar", 3, 254, nothing)
cv2.setTrackbarPos("red color","rgb track bar",125)

img = np.zeros((512,512,3), np.uint8)

while True:
    ret, frame = cam.read()
    redval = cv2.getTrackbarPos("red color", "rgb track bar") + 1
    print(redval)
    res3 = cv2.boxFilter(frame , -1, (redval, redval))
    cv2.imshow('CAM WINDOW', res3)
    cv2.imshow("rgb track bar", img)
    if cv2.waitKey(1) > 0:
        break
cam.release()
cv2.destroyAllWindows()