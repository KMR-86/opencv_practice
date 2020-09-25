import cv2
import numpy as np
import os
print("imports done")

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",179,179,empty)
cv2.createTrackbar("sat min","TrackBars",0,255,empty)
cv2.createTrackbar("sat max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",142,255,empty)

while True:

    h_min=cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("val min", "TrackBars")
    v_max = cv2.getTrackbarPos("val max", "TrackBars")
    print(v_min,v_max)


    img_path = os.path.join(os.path.dirname(__file__), 'resources', 'img1.jpeg')
    print(img_path)
    img = cv2.imread(img_path)
    img = cv2.imread(img_path)
    img = cv2.resize(img,(640,480))

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower=np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    img_result=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("normal", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",img_result)
    cv2.waitKey(1)