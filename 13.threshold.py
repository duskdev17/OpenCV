import cv2 as cv


img = cv.imread('Photos/moscow2.jpg')

cv.imshow('Image', img)



#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)




#simple thresholding
threshold, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)


cv.imshow('Simple Thresholded', thresh)

print(threshold)




cv.waitKey(0)