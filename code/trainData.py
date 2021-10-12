import logging
import os

import cv2
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from dask.tests.test_base import np

from IoTPractice.code.exceptions import RecordNotFound

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


class trainData:
    def __init__(self):
        self.datasets = 'faceData'

    # 检测人脸
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

    def __prepareTrainingData__(self, data_folder_path):
        dirs = os.listdir(data_folder_path)
        faces = []
        labels = []

        face_id = 1
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        # 遍历人脸库
        for dir_name in dirs:
            if not dir_name.startswith('stu_'):
                continue
            stu_id = dir_name.replace('stu_', '')
            try:
                cursor.execute('SELECT * FROM users WHERE stu_id=?', (stu_id,))
                ret = cursor.fetchall()
                if not ret:
                    raise RecordNotFound
                cursor.execute('UPDATE users SET face_id=? WHERE stu_id=?', (face_id, stu_id,))
            except RecordNotFound:
                logging.warning('数据库中找不到名为{}的用户记录'.format(stu_id))
                self.logQueue.put('发现学号为{}的人脸数据，但数据库中找不到相应记录，已忽略'.format(stu_id))
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

        cursor.close()
        conn.commit()
        conn.close()

        return faces, labels

    def trainFaceData(self):
        logging.info('begin to train face data')
        try:
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            if not os.path.exists('./recognizer'):
                os.makedirs('./recognizer')
            faces, labels = self.__prepareTrainingData__(self.datasets)
            face_recognizer.train(faces, np.array(labels))
            face_recognizer.save('./recognizer/trainingData.yml')
        except Exception as e:
            logging.error('遍历人脸库出现异常，训练人脸数据失败')
            self.trainButton.setIcon(QIcon('./icons/error.png'))
            QMessageBox.critical(self, '提示', '遍历人脸库出现异常，训练失败', QMessageBox.Cancel)
        else:
            QMessageBox.info(self, '提示', '人脸数据训练完成', QMessageBox.Yes)
