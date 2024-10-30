import cv2
import numpy as np
import matplotlib.pyplot as plt

arr = np.float32(np.random.rand(255,255,3))
print(arr)

plt.subplot(1,4,1)
plt.imshow(arr)
plt.axis('off')
plt.title('normal')

arr[:] = 0,0,255
plt.subplot(1,4,2)
plt.imshow(arr)
plt.axis('off')
plt.title('Blue')


arr[:] = 0,255,0
plt.subplot(1,4,3)
plt.imshow(arr)
plt.axis('off')
plt.title('Green')

arr[:] = 255,0,0
plt.subplot(1,4,4)
plt.imshow(arr)
plt.axis('off')
plt.title('Red')
plt.show()

blank = np.zeros((500,500,3))
cv2.imshow('blank',blank)

# draw a rectangle box
cv2.rectangle(blank, (2,2), (250,250), (255,0,0), -1)
cv2.imshow('rectangle', blank)

# draw a circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,255,0),-1, 0)
cv2.imshow('circle',blank)

# draw a line
cv2.line(blank,(500,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255),3,2)
cv2.imshow('line', blank)

# putting a text in the image
img = np.zeros((500,500))
cv2.putText(img,"This is JK",(0,125), cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),3,1)

cv2.imshow('text', img)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()