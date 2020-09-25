import cv2
import os
import numpy as np
print("package imported")

def get_contours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>100:
            print("area : ", area)
            cv2.drawContours(img_contour,cnt,-1,(255,0,0),2)
            peri=cv2.arcLength(cnt,True)
            #print("peri : ",peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            objCor=len(approx)
            print("number of sides : ",len(approx))
            #bounding box
            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(img_contour,(x,y),(x+w,y+h),(255,255,0),2)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Sqr"
                else:
                    objectType = "Rect"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img_contour, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 255, 255), 1)


img_path = os.path.join(os.path.dirname(__file__), 'resources', 'img3.png')
print(img_path)
img = cv2.imread(img_path)
img = cv2.resize(img,(640,480))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(7,7),1)
img_edges=cv2.Canny(img_blur,100,100)
img_contour=img.copy()

get_contours(img_edges)
cv2.imshow("object detected",img_contour)
cv2.imshow("original",img)
cv2.waitKey(0)