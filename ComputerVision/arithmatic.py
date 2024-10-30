import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
img2 = cv2.imread(r'C:\Users\jeyak\Downloads\bus2.jpg')

img2 = cv2.resize(img2,(539,360))
print(img1.shape,img2.shape)

plt.subplot(1,4,1)
plt.imshow(img1)
plt.axis('off')
plt.title('img1')

plt.subplot(1,4,2)
plt.imshow(img2)
plt.axis('off')
plt.title('img2')

plt.subplot(1,4,3)
add = cv2.add(img1,img2)
plt.imshow(add)
plt.axis('off')
plt.title('add')

subtract = cv2.subtract(img1,img2)
plt.subplot(1,4,4)
plt.imshow(subtract)
plt.axis('off')
plt.title('subtract')
plt.show()

cv2.imshow('bitwise and',cv2.bitwise_and(img1,img2))
cv2.imshow('bitwise or',cv2.bitwise_or(img1,img2))
cv2.imshow('bitwise xor',cv2.bitwise_xor(img1,img2))
cv2.imshow('bitwise not',cv2.bitwise_not(img1))
cv2.waitKey(0)