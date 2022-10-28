import cv2 as cv
from cv2 import rectangle
from cv2 import bitwise_and
from cv2 import bitwise_or
from cv2 import bitwise_xor
import numpy as np

blank =  np.zeros((400, 400), 'uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)


# Bitwise OR --> non intersecting regions and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)




# Bitwise XOR --> non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)




# Bitwise Not -->  inverts
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)




cv.waitKey(0)


