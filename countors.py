import cv2
import sys
import numpy as np

image = cv2.imread(str(sys.argv[1]),0)
ret,thresh = cv2.threshold(image,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh,1,2)
#_,contours,_,hierarchy= cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)

x,y,w,h = cv2.boundingRect(cnt)
image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow("Image-{}", image)
key = cv2.waitKey(1000)

print M

