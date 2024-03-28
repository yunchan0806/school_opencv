import numpy as np
import cv2
def draw_rect(event, x, y, flage, param):
    print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x,y), (x+50,y+50), (255,0,0), -1)

img = img_color = cv2.imread('images\\img10.png')



while(1):
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw_rect)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()