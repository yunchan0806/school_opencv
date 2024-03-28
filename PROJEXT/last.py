import numpy as np
import cv2
from matplotlib import pyplot as plt
def nothing(x):
    pass
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img_color = cv2.imread('images\\img10.png')
height, width = img_color.shape[:2] 


cv2.namedWindow("trackbar")

cv2.createTrackbar("L_H", "trackbar", 0, 255, nothing)
cv2.createTrackbar("L_S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("L_V", "trackbar", 0, 255, nothing)

cv2.createTrackbar("m", "trackbar", 0, 255, nothing)

cv2.createTrackbar("U_H", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U_S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U_V", "trackbar", 0, 255, nothing)

cv2.setTrackbarPos("L_H", "trackbar", 0)
cv2.setTrackbarPos("L_S", "trackbar", 0)
cv2.setTrackbarPos("L_V", "trackbar", 0)

cv2.setTrackbarPos("U_H", "trackbar", 125)
cv2.setTrackbarPos("U_S", "trackbar", 125)
cv2.setTrackbarPos("U_V", "trackbar", 125)
cv2.setTrackbarPos("m", "trackbar", 125)

while True:
    img_a = cv2.imread('images\\img10.png')

    l_H = cv2.getTrackbarPos("L_H", "trackbar")
    l_S = cv2.getTrackbarPos("L_S", "trackbar")
    l_V = cv2.getTrackbarPos("L_V", "trackbar")

    u_H = cv2.getTrackbarPos("U_H", "trackbar")
    u_S = cv2.getTrackbarPos("U_S", "trackbar")
    u_V = cv2.getTrackbarPos("U_V", "trackbar")
    threshold = (cv2.getTrackbarPos("m", "trackbar")*2)+1

    m = cv2.medianBlur(img_color, threshold)
    img_hsv = cv2.cvtColor(m, cv2.COLOR_BGR2HSV) 

    lower = np.array([l_H, l_S, l_V])
    upper = np.array([u_H, u_S, u_V])
    img_mask = cv2.inRange(img_hsv, lower, upper)
    cv2.imshow('kkk', img_mask)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    dst = cv2.dilate(img_mask, k)


    
    erosion = cv2.erode(dst, k)
    erosion = cv2.erode(erosion, k)

    
    img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask) 
    
    contours, hierarchy = cv2.findContours(img_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    
    for cnt in contours:
    
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)  # Approximate contour with fewer points
        ((x, y), radius) = cv2.minEnclosingCircle(approx)  # Fit circle to the approximated contour
        M = cv2.moments(approx)
        area = cv2.contourArea(approx)

        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            print(center, area)
        else:
            center = (0, 0)
        if radius/2 > 10:
            cv2.circle(img_a, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(img_a, center, 5, (0, 0, 255), -1)
    
    
    

    ret, thresh_cv = cv2.threshold(erosion, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Result', erosion)  # Display merged1 in the results window
    cv2.imshow('img', img_a)  # Display img_a in another window
    cv2.imshow('Threshold Image', thresh_cv) 
    cv2.imshow('img_result', img_result) 
    cv2.imshow('medianBlur', m) 
    key = cv2.waitKey(30)
    if key == 27:  # ESC 키를 누르면 루프 탈출
        break

    
cv2.destroyAllWindows()