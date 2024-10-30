import cv2
import matplotlib.pyplot as plt


def display_image():
    img = cv2.imread(r'C:\Users\jeyak\Downloads\bus1.jpg')
    cv2.imshow('bus',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def display_video():
    video = cv2.VideoCapture(r"C:\Users\jeyak\Downloads\videoplayback.mp4")
    while True:
        _, frame = video.read()
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xfff==ord('c'):
            break


def resize_image():
    img = cv2.imread(r"C:\Users\jeyak\Downloads\bus1.jpg")
    print('original image shape',img.shape)
    plt.subplot(1,2,1)
    plt.imshow(img)
    img_resized = cv2.resize(img,(150,200))
    print('resized image shape', img_resized.shape)
    plt.subplot(1,2,2)
    plt.imshow(img_resized)
    plt.show()


def live_camera():
    live_camera: cv2.VideoCapture = cv2.VideoCapture(0)
    while True:
        _, frame = live_camera.read()
        cv2.imshow('camera',frame)
        if cv2.waitKey(1) & 0xfff == ord('c'):
            break


# To read an image
display_image()

# To read a video from file
display_video()

# To read a video from live camera
live_camera()

# To resize an image
resize_image()


