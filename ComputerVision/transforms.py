import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jeyak\Downloads\pexels-chevanon-1108099.jpg")
# cv2.imshow('original', img)

img = cv2.resize(img, (500,500))
# translation
def translation(img, x, y):
    # -x -> left
    # x -> right
    # y -> down
    # -y -> up
    translation_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img, translation_matrix, dimensions)


translated_image = translation(img, 100, 120)
cv2.imshow('translation', translated_image)


# rotation
def rotation(img, rotPoints, angle):
    if rotPoints is None:
        rotPoints = (img.shape[1]//2, img.shape[0]//2)
    rotation_matrix = cv2.getRotationMatrix2D(rotPoints, angle, 1.0)
    return cv2.warpAffine(img, rotation_matrix, (img.shape[1],img.shape[0]))

rotated_image = rotation(img,None,angle=45)
cv2.imshow('rotation', rotated_image)

# resize
resized = cv2.resize(img,(256,256))
cv2.imshow('resized',resized)

# Flipping
flipped_image = cv2.flip(img, 1)
cv2.imshow('flipped image', flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()