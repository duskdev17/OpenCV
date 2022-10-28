import cv2 as cv
import numpy as np

img = cv.imread('Photos/4.jpg')
cv.imshow('Main Image', img)


blank = np.zeros(img.shape[0:2], dtype='uint8')
cv.imshow('Blank', blank)


# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+100, img.shape[0]//2+100), 255, -1)
cv.imshow('Mask', mask)



masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked_image)




cv.waitKey(0)