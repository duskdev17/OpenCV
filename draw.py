import cv2 as cv
from cv2 import imread
from cv2 import circle
import numpy as np

# img = imread('Photos/4.jpg')
# cv.imshow('Image', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. painting an image specific colour
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# blank[200:300, 300:400] = 0, 255, 255
# cv.imshow('Green', blank)




# 2. Draw Rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=cv.FILLED)
# # cv.imshow('Rectangle', blank)



# # 3. Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 255), thickness=-1)
# cv.imshow('Circle', blank)




# # 4. Draw a line
# cv.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1]*1, blank.shape[0]*1), (0, 0, 255), thickness=3)
# cv.imshow('Line', blank)




# 5. Write text on an image
cv.putText(blank, 'Hello World!', (100, 200), cv.FONT_ITALIC, 1.0, (255, 255, 255), 1)
cv.imshow('Text', blank)






cv.waitKey(0)