import cv2
import numpy as np

img = cv2.imread('images\\img10.png')
h, w = img.shape[:2]
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

lower = (0, 120, 150)
upper = (30, 255, 255)

mask = cv2.inRange(img_hsv, lower, upper)
res = cv2.bitwise_and(img, img, mask=mask)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    
    epsilon = 0.05 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)  # Approximate contour with fewer points
    ((x, y), radius) = cv2.minEnclosingCircle(approx)  # Fit circle to the approximated contour
    M = cv2.moments(approx)
    area = cv2.contourArea(approx)

    if M["m00"] != 0:
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        print(center, area)
    else:
        center = (0, 0)
    if radius > 10:
        cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(img, center, 5, (0, 0, 255), -1)

cv2.imshow('make', mask)
cv2.imshow('res', res)
cv2.imshow('imgs', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
