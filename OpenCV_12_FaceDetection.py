import cv2 as cv
import numpy as np
img =  cv.imread('C:/Users/User 2/Desktop/group.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Group', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=9 )
print("Number of faces: " + str(len(faces_rect)))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=2)
cv.imshow('Detected', img)

cv.waitKey(0)