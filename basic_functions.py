import cv2
import os
import numpy as np
print("package imported")


img_path = os.path.join(os.path.dirname(__file__), 'resources', 'img1.jpeg')
print(img_path)
img = cv2.imread(img_path)
img = cv2.resize(img,(640,480))

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(7,7),0)
img_edges=cv2.Canny(img,100,100)

kernel=np.ones((5,5),np.uint8)
img_dial =cv2.dilate(img_edges,kernel,iterations=1)
cv2.imshow("Output", img_gray)
cv2.imshow("Output2",img_blur)
cv2.imshow("Output3",img_edges)
cv2.imshow("output4",img_dial)

###############################################################
#image reshape and crop
###############################################################
img_crop=img[0:200,200:400]
cv2.imshow("output_crop",img_crop)
cv2.waitKey(0)