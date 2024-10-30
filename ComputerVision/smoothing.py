import cv2
import numpy as np

img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
cv2.imshow('original image', img)

# average blur
avg_blur = cv2.blur(img,(9,9))
cv2.imshow('average blur', avg_blur)

# gaussian blur
gauss = cv2.GaussianBlur(img, (5,5), 200)
cv2.imshow('Gaussian blur', gauss)

# median blur
median_blur = cv2.medianBlur(img, 21)
cv2.imshow("median blur", median_blur)

# Bilateral
bilateral = cv2.bilateralFilter(img, 5, 120,500)
cv2.imshow('Bilateral filter', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()