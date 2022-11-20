import os
import cv2 as cv
import numpy as np



# p = []
# for i in os.listdir(r'E:\OpenCV\Train'):
#     p.append(i)

# print(p)




people = ['ben', 'bob', 'bryan', 'samiha']
DIR = r'E:\OpenCV\Train'

haar_cascade = cv.CascadeClassifier('classifier/haar_face.xml')


features = []
labels  = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training Done ----------------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# print('Length of features: ', len(features))
# print('Length of labels: ', len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('16.face_trained.yml')
np.save('16.features.npy', features)
np.save('16.labels.npy', labels)