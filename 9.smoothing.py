import cv2 as cv
from numpy import average

img = cv.imread('Photos/forest.jpg')
cv.imshow('Image', img)


# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)


# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)



# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)


# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 15)
cv.imshow('Bilateral', bilateral)







cv.waitKey(0)