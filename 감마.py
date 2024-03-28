import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('C:\\Users\\user\\Desktop\\OpenCv\\images\\img5.jpg', 0)

if img1 is None:
    print("no file found")
    exit()


multi_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
log_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
invol_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)
sel_lut = np.full(shape=[256], fill_value=0, dtype=np.uint8)

multi_v = 2; gamma1 = 0.1; gamma2 =0.6
thres1 = 5; thres2= 100

max_v_log = 255/np.log(1+255)
max_v_invol = 255/np.power(255, gamma1)
max_v_sel = 100/ np.power(thres2, gamma2)

for i in range(256):
    val = i * multi_v

    if val > 255 : val = 256
    multi_lut[i] = val
    log_lut[i] = np.round(max_v_log * np.log(1+i))

    invol_lut[i] = np.round(max_v_invol * np.power(i , gamma1))

    if i < thres1 : sel_lut[i] = i
    elif i > thres2 : sel_lut[i] = i
    else: sel_lut[i] = np.round(max_v_sel * np.power(i, gamma2))



ress = []
ress.append(img1)
ress.append(cv2.LUT(img1, multi_lut))
ress.append(cv2.LUT(img1, log_lut))
ress.append(cv2.LUT(img1, invol_lut))
ress.append(cv2.LUT(img1, sel_lut))

titles = ['입력 영상','상수곱','로그변환','거듭제곱','구간 변환']

plt.rc('font', family='Nanum Gotthic')

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

