import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
cv2.imshow('original image', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_hist = cv2.calcHist([gray],[0],None,[250],[0,256])
plt.plot(gray_hist)
plt.title('Histogram')
plt.xlabel('Bins')
plt.xlim([0,256])
plt.show()