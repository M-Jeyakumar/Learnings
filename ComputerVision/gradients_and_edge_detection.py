import cv2
import numpy as np

img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
cv2.imread('original image',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian
lap = cv2.Laplacian(gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('laplacian',lap)

# Sobel
sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely = cv2.Sobel(gray,cv2.CV_64F,0,1)
combined_sobel = cv2.bitwise_or(sobelx,sobely)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y',sobely)
cv2.imshow('Combined Sobel',combined_sobel)

# Canny
canny = cv2.Canny(gray,130,200)
cv2.imshow('Canny',canny)

cv2.waitKey(0)