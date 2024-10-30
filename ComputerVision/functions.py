import cv2

img = cv2.imread(r"C:\Users\jeyak\Downloads\pexels-chevanon-1108099.jpg")

# resizing the image
img = cv2.resize(img,(500,500))

cv2.imshow('original image', img)

# to convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# to blur the image
blur = cv2.GaussianBlur(img,(5,5),3)
cv2.imshow('blur', blur)

# to find the edges in the images
edges = cv2.Canny(gray,120,170)
cv2.imshow('edges', edges)

dilated = cv2.dilate(edges, (4,4))
cv2.imshow('dilated image',dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()