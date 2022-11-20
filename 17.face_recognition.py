import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('E:\OpenCV\classifier\haar_face.xml')


people = ['ben', 'bob', 'bryan', 'samiha']
# features = np.load('16.features.npy', allow_pickle=True)
# labels = np.load('16.labels.npy')


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('16.face_trained.yml')

img = cv.imread(r'E:\OpenCV\Train\samiha\278364307_275591321455311_4179953416169245461_n.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    # faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print('Label', people[label], 'with a confidence of', confidence)

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)






cv.waitKey(0)
