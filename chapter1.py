import cv2
import os

print("package imported")
###############################################################
#show an image
###############################################################
"""img_path = os.path.join(os.path.dirname(__file__), 'resources', 'img1.jpeg')
print(img_path)
img = cv2.imread(img_path)
cv2.imshow("Output", img)
cv2.waitKey(0)"""



###############################################################
#show an video
###############################################################
"""vid_path= os.path.join(os.path.dirname(__file__), 'resources', 'video1.mp4')
print(vid_path)
cap = cv2.VideoCapture(vid_path)
while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

"""


###############################################################
#show webcam
###############################################################

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



