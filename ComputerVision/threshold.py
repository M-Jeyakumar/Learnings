import cv2

img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
cv2.imshow('original image',img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Simple Thresholding
thres, threshold = cv2.threshold(img, 120, 255,cv2.THRESH_BINARY)
cv2.imshow('normal thresholding',threshold)

thres, threshold_inv = cv2.threshold(img, 120,255, cv2.THRESH_BINARY_INV)
cv2.imshow('threshold inverse',threshold_inv)

# Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow('adaptive threshold', adaptive)

adaptive_inv = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,3)
cv2.imshow('adaptive threshold inverse', adaptive_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()