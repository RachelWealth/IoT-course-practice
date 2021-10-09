import json
import os
import sys
import threading

import cv2
from PyQt5.QtGui import QIcon, QImage, QPixmap

from IoTPractice.code.add import Ui_Dialog as add_Dialog
from IoTPractice.code.faceRecognition.signUpHelper import faceRcgHelper, RecordDisturbance
from IoTPractice.code.managerUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QUrl
from IoTPractice.code.managerSQL import managerSQL
import logging
from IoTPractice.code.Serial import Serial
from IoTPractice.code.WarningQDialog import WarningQDialog
from IoTPractice.code.classifier import classifier
from PyQt5.QtWebEngineWidgets import *
from sendDataHelper import sendDataHelper
from shutil import copyfile
from signUp import Ui_Dialog as faceRcg

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

sqlDic = {2: 'cloth', 3: 'flavoring', 4: 'book'}

global TABLE_MAX_COL, datas
TABLE_MAX_COL = 6
datas = 0


class AppWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.result = []
        self.queryTableName = ''  # the name of table we need to query
        self.sqlHelper = managerSQL()
        self.classHelper = classifier()
        self.firstClass = 'cloth'
        self.secondClass = 'color'
        self.thirdClass = ''

        print('---------------set list item response action---------------')
        logging.info('---------------set list item response action---------------')
        # first class list clicked response
        self.listWidget.itemClicked.connect(self.__firstClassClick__)
        # second class list clicked response
        self.listWidget_2.itemClicked.connect(self.__secondClassClick__)
        # third class list clicked response
        self.tableWidget.setEnabled(True)
        self.tableWidget.clicked.connect(self.__thirdClassClick__)
        self.buttonAddMb.clicked.connect(self.__addMember__)

        self.buttonAddObj.clicked.connect(self.__addObject__)
        # self.buttonAddObject.clicked.connect(add_Dialog.show)
        # self.button_add.clicked(self.addObject)

        self.actionlianjie.triggered.connect(self.__connectSerial__)
        # self.action_4.triggered.connect(self.__connectAbout__)

        self.database = './FaceBase.db'
        self.datasets = './faceData'

        self.browser = QWebEngineView()
        # self.browser.load(QUrl('file:///E:/workplace/pycharmWork/IoTPractice/IoTPractice/code/web/templates/welcom.html'))
        self.browser.load(
            QUrl(r'http://localhost:5000/welcom'))
        self.grid = QGridLayout(self.groupBox_2)
        self.grid.addWidget(self.browser)
        self.fileHelper = sendDataHelper()

        print("finish initial")
        logging.info("finish initial")

    def __getRighrtAndSecondClass__(self, firstClass=None):
        if firstClass is None:
            firstClass = self.firstClass
        if firstClass == 'cloth':
            self.rightClass = list(self.classHelper.homeCloth.get(0))
            self.secondClass = self.classHelper.clothEN[0]
        elif firstClass == 'flavoring':
            self.rightClass = list(self.classHelper.homeFlavoring.get(0))
            self.secondClass = self.classHelper.flavoringEN[0]
        elif firstClass == 'book':
            self.rightClass = list(self.classHelper.homeBook.get(0))
            self.secondClass = self.classHelper.bookEN[0]

    def __firstClassClick__(self):
        logging.info('------------------------------')
        num = self.listWidget.selectedIndexes()[0].row()
        print('__objectClick__' + str(num))
        self.firstClass = self.classHelper.homeObj.get(num)
        logging.info('click ' + self.firstClass + 'item')
        print('click ' + self.firstClass + ' item')
        self.__searchHelper__(self.firstClass)
        self.__subClassDisplay__(num)
        # if self.firstClass == 'cloth':
        #     self.rightClass = list(self.classHelper.homeCloth.get(0))
        #     self.secondClass = self.classHelper.clothEN[0]
        # elif self.firstClass == 'flavoring':
        #     self.rightClass = list(self.classHelper.homeFlavoring.get(0))
        #     self.secondClass = self.classHelper.flavoringEN[0]
        # elif self.firstClass == 'book':
        #     self.rightClass = list(self.classHelper.homeBook.get(0))
        #     self.secondClass = self.classHelper.bookEN[0]
        self.__getRighrtAndSecondClass__()
        self.__rightThirdClassShow__()
        self.objSet, self.des = self.sqlHelper.executeQuery1(self.firstClass)
        self.__objFieldShow__()

    def __searchHelper__(self, tableName):
        """
        search the object by its type
        :param tableName: the same with type name
        :return: self.result
        """
        logging.info("search from " + tableName + '...')
        print("search from " + tableName + '...')
        self.queryTableName = tableName
        self.objSet, self.des = self.sqlHelper.executeQuery1(tableName)

    def __subClassDisplay__(self, num):
        """
        this function to dispaly the second class list of every type of object
        :param num: value:cloth-0, flavoring-1, book-2 and so on
        :return:
        """
        logging.info('prepare to show second class classifier')
        print('prepare to show second class classifier')
        self.currentObjectNum = num
        self.myList = list(self.classHelper.home.get(self.currentObjectNum))
        self.listWidget_2.clear()
        self.listWidget_2.addItems(self.myList)

        logging.info('show success')
        print('show success')
        print('---------------')

    def __secondClassClick__(self, qModelIndex):
        """
        click feature area to get more detailed classifier
        :return:
        """
        logging.info('------------------------------')
        num = self.listWidget_2.selectedIndexes()[0].row()
        print('__secondClassClick__' + str(num))
        if self.firstClass == 'cloth':
            self.rightClass = list(self.classHelper.homeCloth.get(num))
            self.secondClass = self.classHelper.clothEN[num]
        elif self.firstClass == 'flavoring':
            self.rightClass = list(self.classHelper.homeFlavoring.get(num))
            self.secondClass = self.classHelper.flavoringEN[num]
        elif self.firstClass == 'book':
            self.rightClass = list(self.classHelper.homeBook.get(num))
            self.secondClass = self.classHelper.bookEN[num]
        logging.info('click ' + self.firstClass + 'item')
        print('click ' + self.firstClass + ' item')
        self.__rightThirdClassShow__()

    def __rightThirdClassShow__(self):
        """
        display of third class classifier
        :return:
        """
        self.tableWidget.clearContents()
        col = 0
        row = 0
        for itemName in self.rightClass:
            if self.firstClass == 'cloth' and self.secondClass == 'color':
                itemName = itemName + '色'
            if col < TABLE_MAX_COL:
                item = QTableWidgetItem(self.tableWidget.item(row, col))
                _translate = QtCore.QCoreApplication.translate
                item.setText(_translate("MainWindow", itemName))
                self.tableWidget.setItem(row, col, item)
                col += 1
            elif col == TABLE_MAX_COL and row < 1:
                col = 0
                row += 1
                item = QTableWidgetItem(self.tableWidget.item(row, col))
                _translate = QtCore.QCoreApplication.translate
                item.setText(_translate("MainWindow", itemName))
                self.tableWidget.setItem(row, col, item)
                col += 1
            elif col == TABLE_MAX_COL and row == 1:
                item = QtWidgets.QTableWidgetItem(itemName)
                self.tableWidget.setItem(row, col, item)

    def __thirdClassClick__(self, qTableIndex):
        self.thirdClass = self.tableWidget.item(qTableIndex.row(), qTableIndex.column()).text()
        logging.info('third class click:' + self.thirdClass)
        print('third class click:' + self.thirdClass)
        if self.secondClass == 'color':
            self.thirdClass = self.thirdClass[0]
        self.objSet, self.des = self.sqlHelper.executeQuery2(self.firstClass, self.secondClass, self.thirdClass)
        self.__objFieldShow__()

    def __objFieldShow__(self):
        """
        this function used to switch the display content
        :return:
        """
        logging.info("load dynamic web")
        print("load dynamic web")
        if len(self.objSet) == 0:
            self.browser.load(QUrl(r'http://localhost:5000/'))
        else:
            self.objList = self.sqlHelper.tupleTOdic(self.objSet, self.des)
            self.objJson = json.dumps(self.objList, ensure_ascii=False)
            # self.objJson = self.objJson[1:len(self.objJson) - 1]
            print(self.objJson)
            self.fileHelper.writeToFile(self.objJson)
            self.browser.load(QUrl(r'http://localhost:5000/index'))
        self.grid.addWidget(self.browser)

        logging.info("load successfully")
        print("load successfully")

    def __voiceManager__(self):
        """
        To process the voice command we get from serial
        :return:
        """
        # self.serial = Serial()
        # self.port = self.serial.getSerial()

        command = self.serialHelper.readSerial()
        if sqlDic.get(command) is not None:
            self.__searchHelper__(sqlDic[command])
            num = list(self.classHelper.homeObj.keys())[list(self.classHelper.homeObj.values()).index('1004')]
            self.__subClassDisplay__(num)
            self.__getRighrtAndSecondClass__()
            self.__rightThirdClassShow__()
            self.objSet, self.des = self.sqlHelper.executeQuery1(self.firstClass)
            self.__objFieldShow__()
        elif command == 1:
            print('小杰')
        elif command == 0:

            # add some process to show this action
            pass
        elif command == -1:
            # WarningQDialog("对不起，我无法识别你的语音")
            pass
        else:
            pass
        print('command=' + str(command))

    def __readSerialDataTimely__(self):
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.__voiceManager__)
        self._timer.start(1000)  # plot after 1s delay

    def __connectSerial__(self):
        self.serialHelper = Serial()
        self.managerSerial = self.serialHelper.getSerial()
        if self.managerSerial == -1:
            QMessageBox.critical(self, '连接语音模块', '无法连接语音模块！', QMessageBox.Ok)
            return 0
        QMessageBox.information(self, '连接语音模块', '语音模块连接成功！', QMessageBox.Ok)

        print('---------------set timeer---------------')
        logging.info('---------------set timeer---------------')
        try:
            threading.Thread(target=self.__readSerialDataTimely__()).start()
        except:
            QMessageBox.information(self, '运行语音模块', '语音模块运行失败！', QMessageBox.Ok)

    def __changeAddWin__(self):
        n = self.addWin.comboBox.currentIndex()
        if n == 0:
            self.addWin.comboBox_2.clear()
            self.addWin.comboBox_3.clear()
            self.addWin.comboBox_4.clear()

            self.addWin.label_2.setText('颜色')
            self.addWin.label_3.setText('物品')
            self.addWin.label_4.setVisible(False)
            self.addWin.label_4.setText('季节')

            self.addWin.comboBox_2.addItems(self.classHelper.ccolor)
            self.addWin.comboBox_3.addItems(self.classHelper.cbrand)
            self.addWin.comboBox_4.setVisible(False)
            self.addWin.comboBox_4.addItems(self.classHelper.cseason)
        elif n == 1:
            self.addWin.comboBox_2.clear()
            self.addWin.comboBox_3.clear()

            self.addWin.label_2.setText('种类')
            self.addWin.label_3.setText('品牌')
            self.addWin.label_4.setVisible(False)

            self.addWin.comboBox_2.addItems(self.classHelper.fkind)
            self.addWin.comboBox_3.addItems(self.classHelper.fbrand)
            self.addWin.comboBox_4.setVisible(False)
        elif n == 2:
            self.addWin.comboBox_2.clear()
            self.addWin.comboBox_3.clear()
            self.addWin.comboBox_4.clear()

            self.addWin.label_2.setText('作者')
            self.addWin.label_3.setText('语言')
            self.addWin.label_4.setVisible(False)
            self.addWin.label_4.setText('出版社')

            self.addWin.comboBox_2.addItems(self.classHelper.bauthor)
            self.addWin.comboBox_3.addItems(self.classHelper.blanguage)
            self.addWin.comboBox_4.setVisible(False)
            self.addWin.comboBox_4.addItems(self.classHelper.bpublisher)

    def __insertPicToFile__(self, n, id, src):
        logging.info('add file: \nsrc-' + src)
        dst = 'E:\\workplace\\pycharmWork\\IoTPractice\\IoTPractice\\code\\web\\static\\img' + self.classHelper.homeObj.get(
            n) + id + '.jpg'
        logging.info('dst:' + dst)
        copyfile(src, dst)
        logging.info('Add picture success')

    def __drapToEdit__(self):
        if 0 == self.textEdit.toPlainText().find('file:///'):
            self.textEdit.setText(self.textEdit.toPlainText().replace('file:///', ''))

    def __getAddContent__(self):
        self.addWin.textEdit.textChanged.connect(self.editchange)
        src = self.addWin.textEdit.toPlainText()
        if ~os.path.exists(src):
            QMessageBox.warning(self, '提交失败', '提交失败，请确认图片路径是否正确', QMessageBox.Cancel)
            return 0
        n = self.addWin.comboBox.currentIndex()
        # TODO change name to the name of account login currently
        user = '王梅'
        id = 0
        if n == 0:
            color = self.addWin.comboBox_2.currentText()
            brand = self.addWin.comboBox_3.currentText()
            season = self.addWin.comboBox_4.currentText()
            id = self.sqlHelper.executeInsertcloth(user=user, gender='女', color=color, brand=brand, season=season)
        elif n == 1:
            kind = self.addWin.comboBox_2.currentText()
            brand = self.addWin.comboBox_3.currentText()
            id = self.sqlHelper.executeInsertFlavoring(user=user, kind=kind, brand=brand)
        elif n == 2:
            author = self.addWin.comboBox_2.currentText()
            language = self.addWin.comboBox_3.currentText()
            publisher = self.addWin.comboBox_4.currentText()
            id = self.sqlHelper.executeInsertBook(user=user, author=author, language=language, publisher=publisher)
        threading.Thread(target=self.__insertPicToFile__(n, id, src)).start()

    def __addObject__(self):
        dia = QtWidgets.QDialog()
        self.addWin = add_Dialog()
        self.addWin.setupUi(dia)
        self.addWin.comboBox.currentIndexChanged.connect(self.__changeAddWin__)
        if dia.exec():  # click OK
            self.__getAddContent__()
        else:  # click CANCEL
            pass

    def __alreadySignUp__(self):
        n = self.addHelper.radioButton.isChecked()
        if n:

            self.addHelper.label_6.setEnabled(False)
            self.addHelper.label_7.setEnabled(False)

            self.addHelper.lineEdit_2.setEnabled(False)
            self.addHelper.lineEdit_3.setEnabled(False)

            self.addHelper.pushButton.setEnabled(False)
            self.addHelper.pushButton_2.setEnabled(True)
        else:

            self.addHelper.label_6.setEnabled(True)
            self.addHelper.label_7.setEnabled(True)

            self.addHelper.lineEdit_2.setEnabled(True)
            self.addHelper.lineEdit_3.setEnabled(True)

    def __signUp__(self):
        if not (self.addHelper.nameInput.hasAcceptableInput() and
                self.addHelper.lineEdit_2.hasAcceptableInput() and
                self.userInfoDialog.lineEdit_3.hasAcceptableInput()):
            QMessageBox.warning(self, '提交失败', '注册失败，请确认信息已输入完整', QMessageBox.Yes)
        elif self.addHelper.lineEdit_2.hasAcceptableInput() != self.userInfoDialog.lineEdit_3.hasAcceptableInput():
            QMessageBox.warning(self, '提交失败', '注册失败，请确认两次输入的密码', QMessageBox.Yes)
        else:
            self.userInfo = {'name': '', 'pwd': ''}
            self.userInfo['name'] = self.addHelper.lineEdit_2.text().strip()
            self.userInfo['pwd'] = self.uaddHelper.lineEdit_2.text().strip()

            self.user_id = self.sqlHelper.executeInsertUser(name=self.userInfo['name'], username=self.userInfo['name'],
                                             password=self.userInfo['pwd'])
            logging.info('成功录入用户信息：' + self.userInfo['name'])
            print('成功录入用户信息：' + self.userInfo['name'])

            self.addHelper.pushButton_2.setEnabled(True)
            self.addHelper.pushButton_2.clicked.connect()

    def __faceRecord__(self):
        if not self.isFaceRecordEnabled:
            self.isFaceRecordEnabled = True

    def __detectFace__(self, frame):
        """
        to detect face at a regular time
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(90, 90))

        name = self.userInfo.get('name')

        for (x, y, w, h) in faces:
            if self.isFaceRecordEnabled:
                try:
                    if not os.path.exists('{}/stu_{}'.format(self.datasets, self.user_id)):
                        os.makedirs('{}/stu_{}'.format(self.datasets, self.user_id))
                    if len(faces) > 1:
                        raise RecordDisturbance

                    cv2.imwrite('{}/stu_{}/img.{}.jpg'.format(self.datasets, self.user_id, self.faceRecordNum + 1),
                                gray[y - 20:y + h + 20, x - 20:x + w + 20])
                except RecordDisturbance:
                    self.isFaceRecordEnabled = False
                    logging.error('检测到多张人脸或环境干扰')
                    self.logQueue.put('Warning：检测到多张人脸或环境干扰，请解决问题后继续')
                    self.enableFaceRecordButton.setIcon(QIcon('./icons/warning.png'))
                    continue
                except Exception as e:
                    logging.error('写入人脸图像文件到计算机过程中发生异常')
                    self.enableFaceRecordButton.setIcon(QIcon('./icons/error.png'))
                    self.logQueue.put('Error：无法保存人脸图像，采集当前捕获帧失败')
                else:
                    self.enableFaceRecordButton.setIcon(QIcon('./icons/success.png'))
                    self.faceRecordNum = self.faceRecordNum + 1
                    self.isFaceRecordEnabled = False
                    self.addHelper.lcdNumber.display(self.faceRecordNum)
            cv2.rectangle(frame, (x - 5, y - 10), (x + w + 5, y + h + 10), (0, 0, 255), 2)
        return frame

    def __updateFrame__(self):
        ret, frame = self.cap.read()
        # self.image = cv2.flip(self.image, 1)
        if ret:
            self.displayImage(frame)

            if self.isFaceDetectEnabled:
                detected_frame = self.detectFace(frame)
                self.displayImage(detected_frame)
            else:
                self.displayImage(frame)

    def __showFacePic__(self, pic):
        # BGR -> RGB
        img = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        self.addHelper.label_3.setPixmap(QPixmap.fromImage(outImage))
        self.addHelper.label_3.setScaledContents(True)

    def __startFaceRecord__(self):
        name = self.addHelper.nameInput.text()
        if name == '':
            self.isUserInfoReady = False
            QMessageBox.warning(self, '提示', '开启失败，请输入用户姓名', QMessageBox.Yes)
            return 0
        if not self.sqlHelper.executeQuery2('user', 'name', name):
            self.isUserInfoReady = False
            QMessageBox.warning(self, '提示', '开启失败，系统中无该用户信息', QMessageBox.Yes)
            return 0
        if self.addHelper.pushButton_2.text() == '开始采集人脸数据':
            # begin detect face at regular time
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.__updateFrame__)
            self.addHelper.radioButton.setEnabled(False)
            self.addHelper.pushButton.setEnabled(False)
            if not self.addHelper.pushButton_4.isEnabled():
                self.addHelper.pushButton_4.setEnabled(True)
            self.addHelper.pushButton_4.setIcon(QIcon())
            self.addHelper.pushButton_4.setIcon(QIcon('./icons/success.png'))
            self.startFaceRecordButton.setText('结束当前人脸采集')
        else:
            if self.faceRecordNum < self.minfaceRecordNum:
                QMessageBox.warning(self, '提示', '请至少采集 100 帧图像。', QMessageBox.Yes)

            else:
                ret = QMessageBox.warning(self, '提示',
                                          '系统当前采集了{}帧图像，继续采集可以提高识别准确率。\n你确定结束当前人脸采集吗？'.format(self.faceRecordNum),
                                          QMessageBox.Yes | QMessageBox.No)

                if ret == QMessageBox.Yes:
                    self.isFaceDataReady = True
                    if self.isFaceRecordEnabled:
                        self.isFaceRecordEnabled = False
                    self.addHelper.pushButton_4.setEnabled(False)
                    self.addHelper.pushButton_2.setText('开始采集人脸数据')
                    self.addHelper.pushButton_2.setEnabled(False)
                    self.addHelper.pushButton_2.setIcon(QIcon())
                    self.migrateToDbButton.setEnabled(True)
                else:
                    self.addHelper.radioButton.setEnabled(True)
                    self.addHelper.pushButton.setEnabled(True)

    def startWebcam(self, status):
        """
        open the camera
        """
        if status:
            if self.isExternalCameraUsed:
                camID = 1
            else:
                camID = 0
            self.cap.open(camID)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            ret, frame = self.cap.read()

            if not ret:
                logging.error('无法调用电脑摄像头{}'.format(camID))
                QMessageBox.warning(self, '提示', '初始化摄像头失败')
                self.cap.release()
            else:
                self.enableFaceDetectButton.setEnabled(True)
                self.timer.start(5)
        else:
            if self.cap.isOpened():
                if self.timer.isActive():
                    self.timer.stop()
                self.cap.release()
                self.faceDetectCaptureLabel.clear()
                self.faceDetectCaptureLabel.setText('<font color=red>摄像头未开启</font>')
                self.enableFaceDetectButton.setEnabled(False)

    def __useExternalCamera__(self, useExternalCameraCheckBox):
        if useExternalCameraCheckBox.isChecked():
            self.isExternalCameraUsed = True
        else:
            self.isExternalCameraUsed = False

    def __addMember__(self):
        print('click add member')
        dia = QtWidgets.QDialog()
        self.addHelper = faceRcg()
        self.addHelper.setupUi(dia)
        self.externCm = False
        self.addHelper.checkBox.stateChanged.connect(lambda: self.__useExternalCamera__(self.useExternalCameraCheckBox))
        self.ifSignUp = False
        self.addHelper.pushButton_2.clicked.connect(self.__startFaceRecord__)
        self.addHelper.radioButton.clicked.connect(self.__alreadySignUp__)
        self.addHelper.pushButton.clicked.connect(self.__signUp__)
        self.addHelper.pushButton_4.clicked.connect(self.__faceRecord__)
        if dia.exec():  # click OK and begin to train and save
            self.__recordFace__()
        else:
            pass
