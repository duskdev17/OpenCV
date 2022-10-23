import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/moscow2.jpg')
cv.imshow('Main Image', img)


# plt.imshow(img)
# plt.show()


# BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# cv.imshow('Gray --> BGR', gray_bgr)



# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)


# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)



# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)




# plt.imshow(rgb)
# plt.show()



cv.waitKey(0)