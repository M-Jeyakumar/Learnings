import cv2
import numpy as np

img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
cv2.imshow('original image', img)
print(img.shape)
blank = np.zeros((img.shape[:2]),dtype='uint8')
cv2.imshow('blank', blank)

rectangle = cv2.rectangle(blank,(130,100),(450,270),255,-1)
cv2.imshow('rectangle shape', rectangle)

masked_image = cv2.bitwise_and(img,img,mask=rectangle)
cv2.imshow('masked image',masked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()