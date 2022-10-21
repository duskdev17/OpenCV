from ctypes import resize
import cv2 as cv

img = cv.imread('Photos/forest.jpg')
cv.imshow('img', img)


# converting to gayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur Image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


# Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


# Dialating Image
dialated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dialated)


# Eroding
eroded = cv.erode(dialated,  (7, 7), iterations=3)
cv.imshow('Eroded', eroded)


# Resize
resized = cv.resize(img, (1600, 1400), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)




# Cropping
cropped = img[150:350, 350:700]
cv.imshow('Cropped', cropped)






cv.waitKey(0)