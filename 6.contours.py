import cv2 as cv
from cv2 import threshold
import numpy as np

img = cv.imread('Photos/moscow.jpg')
cv.imshow('Img', img)


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thres)

contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# contours, hierarchies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours), 'contour(s) found!') 



cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)