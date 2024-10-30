import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jeyak\Downloads\pexels-chevanon-1108099.jpg")
img = cv2.resize(img, (500,500))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

# method 1:::: by using the threshold
ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('thres',thresh)
# print(ret)
# print(thresh)

contours, hierarchies = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(f"no. of countours found is: {contours}")

# to draw contours
blank = np.zeros(img.shape)
cv2.drawContours(blank,contours, -1, (255,0,0), 1)
cv2.imshow('contour', blank)


# method 2:::: by using the gaussian blur and canny
#
# blur = cv2.GaussianBlur(gray,(5,5),3,cv2.BORDER_DEFAULT)
# canny = cv2.Canny(blur,125,175)
# cv2.imshow('canny',canny)
#
# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# print(f"no. of countours found is: {contours}")
#
# # to draw contours
# blank = np.zeros(img.shape)
# cv2.drawContours(blank,contours, -1, (255,0,0), 1)
# cv2.imshow('contour', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()