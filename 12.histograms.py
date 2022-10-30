import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/moscow.jpg')
cv.imshow('Main Image', img)




# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)



blank = np.zeros(img.shape[0:2], dtype='uint8')

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)


# # Gray Histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Gray Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()





# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img],  [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])   


plt.show()


cv.waitKey(0)