import cv2 as cv

img = cv.imread('Photos/2.jpg')
cv.imshow('Img', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)