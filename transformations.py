from turtle import left, right, up
import cv2 as cv
import numpy as np

img = cv.imread('Photos/1.jpg')
cv.imshow('Image', img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x = left
# +x = right
# -y = up
# +y = down


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)




# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)





# Resizing 
resized =  cv.resize(img, (500, 350), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)



# Flip
flipped = cv.flip(img, -1)
cv.imshow('Flipped', flipped)



# Cropped
cropped = img[300:400, 400:600]
cv.imshow('Crop', cropped)













cv.waitKey(0)