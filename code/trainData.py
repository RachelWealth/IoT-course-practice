import logging
import os
import threading

import cv2
from dask.tests.test_base import np
# from cv2 import face

from IoTPractice.code.exceptions import RecordNotFound, traversalError

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


class trainData:
    def __init__(self):
        self.datasets = 'faceData'

    def __detectFace__(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # if self.isEqualizeHistEnabled:
        #     gray = cv2.equalizeHist(gray)
        face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(90, 90))

        if len(faces) == 0:
            return None, None
        (x, y, w, h) = faces[0]
        return gray[y:y + w, x:x + h], faces[0]

    def __prepareTrainingData__(self, data_folder_path, sqlHelper):
        dirs = os.listdir(data_folder_path)
        faces = []
        labels = []

        face_id = 0

        for dir_name in dirs:
            if not dir_name.startswith('mem_'):
                continue
            mem_id = dir_name.replace('mem_', '')
            try:
                # cursor.execute('SELECT * FROM users WHERE face_id=?', (face_id,))
                ret = sqlHelper.executeQuery(table_name='user', key='id', value=mem_id)
                if not ret:
                    raise RecordNotFound
                sqlHelper.executeUpdate(table_name='user', id=ret[0][0], key='face_id', value=face_id)
                # cursor.execute('UPDATE users SET face_id=? WHERE face_id=?', (face_id, face_id,))
            except RecordNotFound:
                logging.warning('数据库中找不到id为{}的用户记录，但是有其人脸信息'.format(face_id))
                continue
            subject_dir_path = data_folder_path + '/' + dir_name
            subject_images_names = os.listdir(subject_dir_path)
            for image_name in subject_images_names:
                if image_name.startswith('.'):
                    continue
                image_path = subject_dir_path + '/' + image_name
                image = cv2.imread(image_path)
                face, rect = self.__detectFace__(image)
                if face is not None:
                    faces.append(face)
                    labels.append(face_id)
            face_id = face_id + 1

        return faces, labels

    def trainFaceData(self, sqlHelper, face_id):
        flag = -1
        logging.info('begin to train face data')
        try:
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            if not os.path.exists('./recognizer'):
                os.makedirs('./recognizer')
            faces, labels = self.__prepareTrainingData__(self.datasets, sqlHelper=sqlHelper)
            face_recognizer.train(faces, np.array(labels))
            face_recognizer.save('./recognizer/trainingData.yml')
        except traversalError:
            logging.error('遍历人脸库出现异常，训练人脸数据失败')
            flag = 1
        else:
            flag = 0
        return flag
