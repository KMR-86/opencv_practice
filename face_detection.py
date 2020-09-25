import cv2
import os
import numpy as np
print("package imported")


img_path = os.path.join(os.path.dirname(__file__), 'resources', 'img1.jpeg')
cascade_path=os.path.join(os.path.dirname(__file__), 'resources', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img=cap.read()

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


    #print(img_path)
    #img = cv2.imread(img_path)
    #img = cv2.resize(img,(640,480))
    #img=img[700:img.shape[0],:]
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    faces=face_cascade.detectMultiScale(img_gray,1.1,4)
    print("number of faces : ",len(faces))
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("video", img)
    #cv2.imshow("output",img)

#cv2.waitKey(0)