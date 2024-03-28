import cv2

cam = cv2.VideoCapture(0)
if cam.isOpened() == False:
    print('Cannot open the camera-%d' % (0))
    exit()
cv2.namedWindow('CAM SINODW')

while True:
    ret, frame = cam.read()
    cv2.imshow('CAM WINDOW', frame)

    if cv2.waitKey(1) > 0:
        break
cam.release()
cv2.destroyAllWindows()