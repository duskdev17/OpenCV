from turtle import width
import cv2 as cv
from cv2 import waitKey
from cv2 import resize

def rescaleFrame(frame, scale=.2):
    #video, image, live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    #live video only/cameras 
    capture.set(3, width)
    capture.set(4, height)



#rescale image
img = cv.imread('Photos/1.jpg')

cv.imshow('Image', img)

resized_image = rescaleFrame(img, scale=0.5)

cv.imshow('ResizedImage', resized_image)

cv.waitKey(0)




#rescale video
capture = cv.VideoCapture('Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('CatVideo', frame)
    cv.imshow('ResizedVideo', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('w'):
        break

capture.release()
cv.destroyAllWindows()