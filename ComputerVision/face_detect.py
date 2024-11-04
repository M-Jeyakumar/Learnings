import cv2
import os

img = cv2.imread(r"C:\Users\jeyak\Downloads\719.jpg")
cv2.imshow('boy image',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haarcascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

detect = haarcascade.detectMultiScale(gray,1.1,6)
for (x,y,w,h) in detect:
    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow('detected face',img)
cv2.waitKey(0)

# print(os.listdir(cv2.data.haarcascades))