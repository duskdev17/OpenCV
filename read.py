import cv2 as cv

# img = cv.imread('Photos/1.jpg')

# cv.imshow('hello', img)

# cv.waitKey(0)


capture = cv.VideoCapture('Videos/cat.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('w'):
        break

capture.release()
cv.destroyAllWindows()

