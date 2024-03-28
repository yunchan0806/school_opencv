import numpy as np
import cv2

def nothing(x):
    pass
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img_color = cv2.imread('images\\img10.png') 
height, width = img_color.shape[:2] 
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) 

cv2.namedWindow("trackbar")

cv2.createTrackbar("L_H", "trackbar", 0, 255, nothing)
cv2.createTrackbar("L_S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("L_V", "trackbar", 0, 255, nothing)

cv2.createTrackbar("U_H", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U_S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U_V", "trackbar", 0, 255, nothing)

cv2.setTrackbarPos("L_H", "trackbar", 0)
cv2.setTrackbarPos("L_S", "trackbar", 0)
cv2.setTrackbarPos("L_V", "trackbar", 0)

cv2.setTrackbarPos("U_H", "trackbar", 125)
cv2.setTrackbarPos("U_S", "trackbar", 125)
cv2.setTrackbarPos("U_V", "trackbar", 125)

while True:
    l_H = cv2.getTrackbarPos("L_H", "trackbar")
    l_S = cv2.getTrackbarPos("L_S", "trackbar")
    l_V = cv2.getTrackbarPos("L_V", "trackbar")

    u_H = cv2.getTrackbarPos("U_H", "trackbar")
    u_S = cv2.getTrackbarPos("U_S", "trackbar")
    u_V = cv2.getTrackbarPos("U_V", "trackbar")

    lower = np.array([l_H, l_S, l_V])
    upper = np.array([u_H, u_S, u_V])
    img_mask = cv2.inRange(img_hsv, lower, upper)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask) 
    dst = cv2.dilate(img_mask, k)


    merged = np.hstack((img_mask, dst))

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    erosion = cv2.erode(merged, k)
    merged1 = np.hstack((merged, erosion))
    cv2.imshow('Erode', merged1)

    cv2.imshow('Dilation', merged)
    cv2.imshow('img_color', img_color)
    cv2.imshow('img_mask', img_mask)
    cv2.imshow('img_color', img_result)

    cv2.waitKey(30)
cv2.destroyAllWindows()