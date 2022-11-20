import cv2 as cv
import numpy as np



#img = cv.imread('Photos/moscow2.jpg')
img = cv.imread('Photos/forest.jpg')
cv.imshow('Image', img)




# convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)






# laplacian edges
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)














cv.waitKey(0)