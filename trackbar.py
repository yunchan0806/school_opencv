import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("rgb track bar")

cv2.createTrackbar("red color", "rgb track bar", 0, 255, nothing)
cv2.createTrackbar("green color", "rgb track bar", 0, 255, nothing)
cv2.createTrackbar("blue color", "rgb track bar", 0, 255, nothing)

cv2.setTrackbarPos("red color","rgb track bar",125)
cv2.setTrackbarPos("green color","rgb track bar",125)
cv2.setTrackbarPos("blue color","rgb track bar",125)

img = np.zeros((512,512,3), np.uint8)

while(1):
    redval = cv2.getTrackbarPos("red color", "rgb track bar")
    greenval = cv2.getTrackbarPos("green color", "rgb track bar")
    blueval = cv2.getTrackbarPos("blue color", "rgb track bar")

    print(redval)

    cv2.rectangle(img, (0,0), (512,512), (blueval, greenval, redval), -1)
    cv2.imshow("rgb track bar", img)

    if cv2.waitKey(30) & 0xFF == 27:
        break
