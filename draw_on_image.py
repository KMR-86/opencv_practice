import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
cv2.imshow("black",img)

img_r=img.copy()
img_r[:]=0,0,255
cv2.imshow("red",img_r)

img_g=img.copy()
img_g[:]=0,255,0
cv2.imshow("green",img_g)

img_rand=img.copy()
img_rand[:]=150,50,86
cv2.imshow("my roll color ",img_rand)

img_draw=cv2.line(img,(0,0),(200,200),(0,255,255),2)
cv2.rectangle(img_draw,(0,0),(250,350),(0,0,255),2)
cv2.circle(img_draw,(300,300),20,(255,255,255),2)
cv2.putText(img_draw,"Mushi",(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
cv2.imshow("draw",img_draw)

#warp images means to get the birds eye view of a cropped part of the image. code not given

#image adding

img_hor=np.hstack((img_r,img_rand))
cv2.imshow("horizontal added image",img_hor)
cv2.waitKey(0)