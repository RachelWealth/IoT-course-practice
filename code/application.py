import json
import os
import shutil
import threading
import dlib

import cv2
from PyQt5.QtGui import QIcon, QImage, QPixmap

from IoTPractice.code.exceptions import unexpectedError, traversalError
from IoTPractice.code.signinWidget import signinWidget
from IoTPractice.code.trainData import trainData
from IoTPractice.code.ui.add import Ui_Dialog as add_Dialog
from IoTPractice.code.faceRecognition.signUpHelper import RecordDisturbance
from IoTPractice.code.ui.managerUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QUrl, QThread
from IoTPractice.code.managerSQL import managerSQL
import logging
from IoTPractice.code.Serial import Serial
from IoTPractice.code.WarningQDialog import WarningQDialog
from IoTPractice.code.classifier import classifier
from PyQt5.QtWebEngineWidgets import *
from sendDataHelper import sendDataHelper
from ui.signin import Ui_Dialog as faceRcg
from ui.login import Ui_Dialog as loginWin
import queue

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

sqlDic = {2: 'cloth', 3: 'flavoring', 4: 'book'}

global TABLE_MAX_COL, datas, id_
TABLE_MAX_COL = 6
datas = 0


class AppWindow(QMainWindow, Ui_MainWindow):
    sqlHelper = managerSQL()
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.result = []
        self.queryTableName = ''  # the name of table we need to query
        
        self.classHelper = classifier()
        self.firstClass = 'cloth'
        self.secondClass = 'color'
        self.thirdClass = ''
        self.isAccountLogIn = False
        self.currntAccount = '王梅'

        print('---------------set list item response action---------------')
        logging.info('set list item response action')

        # first class list clicked response
        self.listWidget.itemClicked.connect(self.__firstClassClick__)

        # second class list clicked response
        self.listWidget_2.itemClicked.connect(self.__secondClassClick__)

        # third class list clicked response
        self.tableWidget.setEnabled(True)

        # third class click
        self.tableWidget.clicked.connect(self.__thirdClassClick__)

        # new menber sign in
        self.buttonAddMb.clicked.connect(self.__addMember__)

        # login
        self.buttonLogIn.clicked.connect(self.__logIn__)

        # add object
        self.buttonAddObj.clicked.connect(self.__addObject__)

        # connect with serial
        self.actionlianjie.triggered.connect(self.__connectSerial__)

        self.datasets = 'faceData'

        # web page display
        self.browser = QWebEngineView()
        logging.info('load welcom page...')
        print('load welcom page...')
        self.browser.load(QUrl(r'http://localhost:5000/welcom'))
        logging.info('load welcom page success')
        print('load welcom page success')
        self.grid = QGridLayout(self.groupBox_2)
        self.grid.addWidget(self.browser)
        self.fileHelper = sendDataHelper()

        print("finish application initial")
        logging.info("finish application initial")

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
        self.objSet, self.des = sqlHelper.executeQuery(self.firstClass)
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
        self.objSet, self.des = sqlHelper.executeQuery(tableName)

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

    def __secondClassClick__(self):
        # def __secondClassClick__(self, qModelIndex):
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
        self.objSet, self.des = sqlHelper.executeQuery(self.firstClass, self.secondClass, self.thirdClass)
        self.__objFieldShow__()

    def __startWebCamFaceRcg__(self):
        if not self.cap.isOpened():
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
                self.logQueue.put('Error：初始化摄像头失败')
                self.cap.release()
                self.startWebcamButton.setIcon(QIcon('./icons/error.png'))
            else:
                self.faceRcgHelper.start()
                self.timer.start(5)
        else:
            self.faceRcgHelper.stop()
            if self.cap.isOpened():
                if self.timer.isActive():
                    self.timer.stop()
                self.cap.release()

            self.loginHelper.label_3.clear()
            self.loginHelper.label_3.setText('请开启摄像头')

    def __updateFrameRcg__(self):
        if self.cap.isOpened():
            # ret, frame = self.cap.read()
            # if ret:
            #     self.showImg(frame, self.realTimeCaptureLabel)
            if not self.captureQueue.empty():
                captureData = self.captureQueue.get()
                realTimeFrame = captureData.get('realTimeFrame')
                self.__showFacePic__(realTimeFrame, 'loginHelper')
                self.loginName = self.faceRcgHelper.name
        if self.loginName != '':
            ret = QMessageBox.information(self, '人脸识别登录', '登录名：' + self.loginName, QMessageBox.Yes)
            if ret == QMessageBox.Yes:
                self.dia.close()

    def __faceRcgPro__(self):
        self.isExternalCameraUsed = False
        self.cap = cv2.VideoCapture()
        self.captureQueue = queue.Queue()
        self.faceRcgHelper = faceRcgLogin(self.cap, self.captureQueue)
        self.loginName = self.faceRcgHelper.name
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__updateFrameRcg__)

        self.__startWebCamFaceRcg__()

    def __loginByTwoMethod__(self):
        if self.loginHelper.tabWidget.currentIndex() == 0:
            pass
        else:
            self.__faceRcgPro__()
            # self.dia.close()

    def __logIn__(self):
        self.dia = QtWidgets.QDialog()
        self.loginHelper = loginWin()
        self.loginHelper.setupUi(self.dia)
        # self.loginHelper = signinWidget()

        self.loginHelper.tabWidget.setCurrentIndex(0)
        self.loginHelper.checkBoxUseExterCam.stateChanged.connect(
            lambda: self.__useExternalCamera__(self.loginHelper.checkBoxUseExterCam))
        self.loginHelper.tabWidget.currentChanged['int'].connect(self.__loginByTwoMethod__)
        # if self.dia.exec():
        if self.dia.exec():
            if self.loginHelper.tabWidget.currentIndex() == 0:  # login by password
                # TODO close cap
                name = self.loginHelper.inputUserName.text().strip()
                pwd = self.loginHelper.inputPwd.text().strip()
                [result, _] = sqlHelper.executeQuery(table_name='user', name=name, key='password', value=pwd)
                if len(result) == 0:
                    WarningQDialog('密码或用户名错误，请检查账户名是否存在，密码是否正确')
                else:
                    self.currntAccount = name
                    self.buttonLogIn.setText(self.currntAccount)
                    self.labelID.setText('ID号：' + str(result[0][0]))
                    self.browser.load(QUrl(r'http://localhost:5000/welcom'))
            else:  # login by face recognition

                print('人脸识别登录')
        else:
            pass

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
            self.objList = sqlHelper.tupleTOdic(self.objSet, self.des)
            self.objJson = json.dumps(self.objList, ensure_ascii=False)
            # self.objJson = self.objJson[1:len(self.objJson) - 1]
            print(self.objJson)
            self.fileHelper.writeToFile(self.objJson)
            # TODO reverse order
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
            self.objSet, self.des = sqlHelper.executeQuery(self.firstClass)
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
            self.addWin.label_4.setVisible(True)
            self.addWin.label_4.setText('季节')

            self.addWin.comboBox_2.addItems(self.classHelper.ccolor)
            self.addWin.comboBox_3.addItems(self.classHelper.cbrand)
            self.addWin.comboBox_4.setVisible(True)
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
            self.addWin.label_4.setVisible(True)
            self.addWin.label_4.setText('出版社')

            self.addWin.comboBox_2.addItems(self.classHelper.bauthor)
            self.addWin.comboBox_3.addItems(self.classHelper.blanguage)
            self.addWin.comboBox_4.setVisible(True)
            self.addWin.comboBox_4.addItems(self.classHelper.bpublisher)

    def __insertPicToFile__(self, n, objID, src):
        logging.info('add file: \nsrc-' + src)
        dst = 'E:\\workplace\\pycharmWork\\IoTPractice\\IoTPractice\\code\\web\\static\\img\\' + self.classHelper.homeObj.get(
            n) + '\\' + str(objID) + '.jpg'
        logging.info('dst:' + dst)
        shutil.copy(src, dst)
        self.isAddObjectSuc = True
        logging.info('Add picture success')

    def __drapToEdit__(self):
        if 0 == self.addWin.textEdit.toPlainText().find('file:///'):
            self.addWin.textEdit.setText(self.addWin.textEdit.toPlainText().replace('file:///', ''))

    def __recordInfoToSql__(self, n, src, user, gender, color=None, brand=None, kind=None, language=None, author=None,
                            publisher=None, season=None):
        objID = 0
        if n == 0:
            objID = sqlHelper.executeInsertcloth(user=user, gender=gender, color=color, brand=brand, season=season)
        elif n == 1:
            objID = sqlHelper.executeInsertFlavoring(user=user, kind=kind, brand=brand)
        elif n == 2:
            objID = sqlHelper.executeInsertBook(user=user, author=author, language=language, publisher=publisher)
        self.__insertPicToFile__(n, objID, src)

    def __getAddContent__(self):
        self.isAddObjectSuc = False
        self.src = self.addWin.textEdit.toPlainText()

        if not os.path.exists(self.src):
            QMessageBox.warning(self, '提交失败', '提交失败，请确认图片路径是否正确', QMessageBox.Cancel)
            return 0
        n = self.addWin.comboBox.currentIndex()
        # TODO change name to the name of account login currently
        color, brand, season, kind, author, language, publisher = [None, None, None, None, None, None, None]
        if n == 0:
            color = self.addWin.comboBox_2.currentText()
            brand = self.addWin.comboBox_3.currentText()
            season = self.addWin.comboBox_4.currentText()
        elif n == 1:
            kind = self.addWin.comboBox_2.currentText()
            brand = self.addWin.comboBox_3.currentText()
        elif n == 2:
            author = self.addWin.comboBox_2.currentText()
            language = self.addWin.comboBox_3.currentText()
            publisher = self.addWin.comboBox_4.currentText()
        # threading.Thread(target=self.__recordInfoToSql__(n=n, user=self.currntAccount, gender='女', color=color, brand=brand, season=season,kind=kind, language=language, publisher=publisher, author=author)).start()
        self.__recordInfoToSql__(n=n, user=self.currntAccount, src=self.src.replace('/', '\\\\'), gender='女',
                                 color=color, brand=brand, season=season,
                                 kind=kind, language=language, publisher=publisher, author=author)

    def __addObject__(self):
        dia = QtWidgets.QDialog()
        self.addWin = add_Dialog()
        self.addWin.setupUi(dia)
        self.addWin.comboBox.currentIndexChanged.connect(self.__changeAddWin__)
        self.addWin.textEdit.textChanged.connect(self.__drapToEdit__)

        if dia.exec():  # click OK
            if self.currntAccount == '':
                WarningQDialog('请登陆后再进行相关操作')
            else:
                self.__getAddContent__()
                if self.isAddObjectSuc:
                    QMessageBox.information(self, '提示', '物品添加成功', QMessageBox.Yes)
        else:  # click CANCEL
            pass

    def __alreadySignUp__(self):
        n = self.addHelper.radioButton.isChecked()
        if n:
            self.addHelper.label_6.setEnabled(False)
            self.addHelper.label_7.setEnabled(False)

            self.addHelper.inputPwd.setEnabled(False)
            self.addHelper.inputConfirmPwd.setEnabled(False)

            self.addHelper.buttonSignIn.setEnabled(False)
            self.addHelper.beginRecordFace.setEnabled(True)
            self.isAlreadySignin = True
        else:

            self.addHelper.label_6.setEnabled(True)
            self.addHelper.label_7.setEnabled(True)

            self.addHelper.inputPwd.setEnabled(True)
            self.addHelper.inputConfirmPwd.setEnabled(True)
            self.isAlreadySignin = False

    def __signUp__(self):
        if not (self.addHelper.inputName.hasAcceptableInput() and
                self.addHelper.inputPwd.hasAcceptableInput() and
                self.addHelper.inputConfirmPwd.hasAcceptableInput()):
            QMessageBox.warning(self, '提交失败', '注册失败，请确认信息已输入完整', QMessageBox.Yes)
        elif self.addHelper.inputPwd.hasAcceptableInput() != self.addHelper.inputConfirmPwd.hasAcceptableInput():
            QMessageBox.warning(self, '提交失败', '注册失败，请确认两次输入的密码', QMessageBox.Yes)
        else:
            self.userInfo = {'name': self.addHelper.inputName.text().strip(),
                             'pwd': self.addHelper.inputPwd.text().strip()}
            # TODO do it in threading
            [result, _] = sqlHelper.executeQuery(table_name='user', key='name', value=self.userInfo.get('name'))
            if len(result) != 0:
                WarningQDialog('用户已存在')
                return 0
            threading.Thread(target=sqlHelper.executeInsertUser(name=self.userInfo.get('name'),
                                                                     password=self.userInfo.get('pwd'))).start()
            logging.info('成功录入用户信息：' + self.userInfo['name'])
            print('成功录入用户信息：' + self.userInfo['name'])
            QMessageBox.information(self, '注册', '注册成功！', QMessageBox.Yes)

            self.addHelper.beginRecordFace.setEnabled(True)
            self.addHelper.beginRecordFace.clicked.connect(self.__startFaceRecord__)

    def __faceRecord__(self):
        if not self.isFaceRecordEnabled:
            self.isFaceRecordEnabled = True

    def __detectFace__(self, frame):
        """
        to detect face at a regular time
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(90, 90))

        self.newId = sqlHelper.reUserId

        for (x, y, w, h) in faces:
            if self.isFaceRecordEnabled:
                try:
                    if not os.path.exists('{}/mem_{}'.format(self.datasets, self.newId)):
                        os.makedirs('{}/mem_{}'.format(self.datasets, self.newId))
                    if len(faces) > 1:
                        raise RecordDisturbance

                    cv2.imwrite('{}/mem_{}/img.{}.jpg'.format(self.datasets, self.newId, self.faceRecordNum + 1),
                                gray[y - 20:y + h + 20, x - 20:x + w + 20])
                except RecordDisturbance:
                    self.isFaceRecordEnabled = False
                    logging.error('检测到多张人脸或环境干扰')
                    self.logQueue.put('Warning：检测到多张人脸或环境干扰，请解决问题后继续')
                    self.addHelper.recordFace.setIcon(QIcon('./icons/warning.png'))
                    continue
                except Exception:
                    logging.error('写入人脸图像文件到计算机过程中发生异常')
                    self.addHelper.recordFace.setIcon(QIcon('./icons/error.png'))
                    self.logQueue.put('Error：无法保存人脸图像，采集当前捕获帧失败')
                else:
                    self.addHelper.recordFace.setIcon(QIcon('./icons/success.png'))
                    self.faceRecordNum = self.faceRecordNum + 1
                    self.isFaceRecordEnabled = False
                    self.addHelper.lcdNumber.display(self.faceRecordNum)
            cv2.rectangle(frame, (x - 5, y - 10), (x + w + 5, y + h + 10), (0, 0, 255), 2)
        return frame

    def __updateFrame__(self):
        ret, frame = self.cap.read()
        # self.image = cv2.flip(self.image, 1)
        if ret:

            detected_frame = self.__detectFace__(frame)
            self.__showFacePic__(detected_frame, 'addHelper')
        else:
            self.__showFacePic__(frame, 'addHelper')

    def __showFacePic__(self, pic, helper):
        # BGR -> RGB
        img = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        if helper == 'addHelper':
            self.addHelper.label_3.setPixmap(QPixmap.fromImage(outImage))
            self.addHelper.label_3.setScaledContents(True)
        else:
            self.loginHelper.label_3.setPixmap(QPixmap.fromImage(outImage))
            self.loginHelper.label_3.setScaledContents(True)

    def __startFaceRecord__(self):
        name = self.addHelper.inputName.text()
        if name == '':
            self.isUserInfoReady = False
            QMessageBox.warning(self, '提示', '开启失败，请输入用户姓名', QMessageBox.Yes)
            return 0
        [result, _] = sqlHelper.executeQuery('user', 'name', name)

        if len(result) == 0:
            self.isUserInfoReady = False
            QMessageBox.warning(self, '提示', '开启失败，系统中无该用户信息', QMessageBox.Yes)
            return 0
        if result[0][3] == 1:
            WarningQDialog('您已有人脸信息')
            return 0
        if self.addHelper.beginRecordFace.text() == '开始录入人脸数据':
            # begin detect face at regular time
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.__updateFrame__)
            self.addHelper.radioButton.setEnabled(False)
            self.addHelper.buttonSignIn.setEnabled(False)
            if not self.addHelper.recordFace.isEnabled():
                self.addHelper.recordFace.setEnabled(True)
            self.addHelper.recordFace.setIcon(QIcon())
            self.addHelper.recordFace.setIcon(QIcon('./icons/success.png'))
            self.addHelper.beginRecordFace.setText('结束当前人脸采集')
            self.__startWebcam__(True)
        else:
            if self.faceRecordNum < self.minfaceRecordNum:
                WarningQDialog('请至少采集 100 帧图像。')
            else:
                ret = QMessageBox.warning(self, '提示',
                                          '系统当前采集了{}帧图像，继续采集可以提高识别准确率。\n你确定结束当前人脸采集吗？'.format(self.faceRecordNum),
                                          QMessageBox.Yes | QMessageBox.No)

                if ret == QMessageBox.Yes:
                    self.isFaceDataReady = True
                    if self.isFaceRecordEnabled:
                        self.isFaceRecordEnabled = False
                    self.addHelper.recordFace.setEnabled(False)
                    self.addHelper.beginRecordFace.setText('开始采集人脸数据')
                    self.addHelper.beginRecordFace.setEnabled(False)
                    self.addHelper.beginRecordFace.setIcon(QIcon())
                    self.migrateToDbButton.setEnabled(True)
                else:
                    self.addHelper.radioButton.setEnabled(True)
                    self.addHelper.buttonSignIn.setEnabled(True)
                    self.__startWebcam__(False)

    def __startWebcam__(self, status):
        """
            open the camera
            :param: status->true:open camera
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

    def __deleteFile__(self):
        [result, _] = sqlHelper.executeQuery(table_name='user', key='name', value=self.addHelper.inputName.text())
        if len(result) == 0:
            pass
        elif os.path.exists('{}/mem_{}'.format(self.datasets, result[0][0])):
            shutil.rmtree('{}/mem_{}'.format(self.datasets, self.newId))

    def __trainFaceData__(self):
        QMessageBox.warning(self, '提示', '系统正在进行人脸数据训练，请勿关闭窗口', QMessageBox.Yes)
        flag = trainData().trainFaceData(sqlHelper=sqlHelper, mem_id=self.newId)
        return flag

    def __addMember__(self):
        print('click add member')
        dia = QtWidgets.QDialog()
        self.addHelper = faceRcg()
        self.addHelper.setupUi(dia)
        self.addHelper.buttonBox.button(QDialogButtonBox.Ok).setText('训练')
        self.cap = cv2.VideoCapture()
        self.faceCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

        self.isFaceRecordEnabled = False
        self.isExternalCameraUsed = False
        self.externCm = False
        self.faceRecordNum = 0
        self.minfaceRecordNum = 100
        # TODO newid=-1
        self.newId = 4

        # TODO add delete member function
        self.isAlreadySignin = False
        self.addHelper.useExternalCameraCheckBox.stateChanged.connect(
            lambda: self.__useExternalCamera__(self.addHelper.useExternalCameraCheckBox))
        self.ifSignUp = False
        self.addHelper.beginRecordFace.clicked.connect(self.__startFaceRecord__)
        self.addHelper.radioButton.clicked.connect(self.__alreadySignUp__)
        self.addHelper.buttonSignIn.clicked.connect(self.__signUp__)
        self.addHelper.recordFace.clicked.connect(self.__faceRecord__)
        if dia.exec():  # click OK and begin to train and save
            # TODO add progress bar
            flag = self.__trainFaceData__()
            if flag == -1:
                raise unexpectedError
            elif flag == 1:
                raise traversalError
            else:
                QMessageBox.information(self, '提示', '人脸数据训练成功', )
        else:
            self.timer.timeout.disconnect(self.__updateFrame__)
            self.cap.release()
            if self.addHelper.inputName == '':
                pass
            else:
                threading.Thread(target=self.__deleteFile__()).start()

    def closeEvent(self, event):
        sqlHelper.close()
        event.accept()


class faceRcgLogin(QThread):
    trainingData = './recognizer/trainingData.yml'
    sqlHelper = managerSQL()
    def __init__(self, cap, captureQueue):
        super(faceRcgLogin, self).__init__()
        self.isRunning = True
        self.isFaceTrackerEnabled = True
        self.isFaceRecognizerEnabled = True
        self.isPanalarmEnabled = True
        self.name = ''
        self.isDebugMode = False
        self.confidenceThreshold = 50  # confidence coefficience
        self.autoAlarmThreshold = 65
        self.cap = cap
        self.captureQueue = captureQueue

        self.isEqualizeHistEnabled = False

    # # 是否开启人脸跟踪
    # def enableFaceTracker(self, coreUI):
    #     if coreUI.faceTrackerCheckBox.isChecked():
    #         self.isFaceTrackerEnabled = True
    #         coreUI.statusBar().showMessage('人脸跟踪：开启')
    #     else:
    #         self.isFaceTrackerEnabled = False
    #         coreUI.statusBar().showMessage('人脸跟踪：关闭')

    def run(self):
        global recognizer
        faceCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

        # 帧数、人脸ID初始化
        frameCounter = 0
        currentFaceID = 0

        # 人脸跟踪器字典初始化
        faceTrackers = {}

        isTrainingDataLoaded = False
        # isDbConnected = False

        while self.isRunning:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 是否执行直方图均衡化
                # if self.isEqualizeHistEnabled:
                #     gray = cv2.equalizeHist(gray)
                faces = faceCascade.detectMultiScale(gray, 1.3, 5, minSize=(90, 90))

                # 预加载数据文件
                if not isTrainingDataLoaded and os.path.isfile(self.trainingData):
                    recognizer = cv2.face.LBPHFaceRecognizer_create()
                    recognizer.read(self.trainingData)
                    isTrainingDataLoaded = True
                # if not isDbConnected and os.path.isfile(AppWindow.database):
                #     conn = sqlite3.connect(AppWindow.database)
                #     cursor = conn.cursor()
                #     isDbConnected = True

                captureData = {}
                realTimeFrame = frame.copy()
                # alarmSignal = {}

                # 人脸跟踪
                # Reference：https://github.com/gdiepen/face-recognition
                if self.isFaceTrackerEnabled:

                    # 要删除的人脸跟踪器列表初始化
                    fidsToDelete = []

                    for fid in faceTrackers.keys():
                        # 实时跟踪
                        trackingQuality = faceTrackers[fid].update(realTimeFrame)
                        # 如果跟踪质量过低，删除该人脸跟踪器
                        if trackingQuality < 7:
                            fidsToDelete.append(fid)

                    # 删除跟踪质量过低的人脸跟踪器
                    for fid in fidsToDelete:
                        faceTrackers.pop(fid, None)

                    for (_x, _y, _w, _h) in faces:
                        isKnown = False

                        if self.isFaceRecognizerEnabled:
                            cv2.rectangle(realTimeFrame, (_x, _y), (_x + _w, _y + _h), (232, 138, 30), 2)
                            mem_id, confidence = recognizer.predict(gray[_y:_y + _h, _x:_x + _w])
                            logging.debug('mem_id：{}，confidence：{}'.format(mem_id, confidence))

                            # 从数据库中获取识别人脸的身份信息
                            try:
                                result = AppWindow.sqlHelper.executeQuery(table_name='user', key='id', value=mem_id)
                                # cursor.execute("SELECT * FROM users WHERE mem_id=?", (mem_id,))
                                # result = cursor.fetchall()

                                if result:
                                    # name = result[0][3]
                                    self.name = result[0][1]
                                else:
                                    raise Exception
                            except Exception:
                                logging.error('读取数据库异常，系统无法获取Face ID为{}的身份信息'.format(mem_id))
                                # AppWindow.logQueue.put('Error：读取数据库异常，系统无法获取Face ID为{}的身份信息'.format(mem_id))

                                self.name = ''

                            # 若置信度评分小于置信度阈值，认为是可靠识别
                            if confidence < self.confidenceThreshold:
                                isKnown = True
                                cv2.putText(realTimeFrame, self.name, (_x - 5, _y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (0, 97, 255), 2)

                            else:
                                cv2.putText(realTimeFrame, 'unknown', (_x - 5, _y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                            (0, 0, 255), 2)

                        # 帧数自增
                        frameCounter += 1

                        # 每读取10帧，检测跟踪器的人脸是否还在当前画面内
                        if frameCounter % 10 == 0:
                            # 这里必须转换成int类型，因为OpenCV人脸检测返回的是numpy.int32类型，
                            # 而dlib人脸跟踪器要求的是int类型
                            x = int(_x)
                            y = int(_y)
                            w = int(_w)
                            h = int(_h)

                            # 计算中心点
                            x_bar = x + 0.5 * w
                            y_bar = y + 0.5 * h

                            # matchedFid表征当前检测到的人脸是否已被跟踪
                            matchedFid = None

                            for fid in faceTrackers.keys():
                                # 获取人脸跟踪器的位置
                                # tracked_position 是 dlib.drectangle 类型，用来表征图像的矩形区域，坐标是浮点数
                                tracked_position = faceTrackers[fid].get_position()
                                # 浮点数取整
                                t_x = int(tracked_position.left())
                                t_y = int(tracked_position.top())
                                t_w = int(tracked_position.width())
                                t_h = int(tracked_position.height())

                                # 计算人脸跟踪器的中心点
                                t_x_bar = t_x + 0.5 * t_w
                                t_y_bar = t_y + 0.5 * t_h

                                # 如果当前检测到的人脸中心点落在人脸跟踪器内，且人脸跟踪器的中心点也落在当前检测到的人脸内
                                # 说明当前人脸已被跟踪
                                if ((t_x <= x_bar <= (t_x + t_w)) and (t_y <= y_bar <= (t_y + t_h)) and
                                        (x <= t_x_bar <= (x + w)) and (y <= t_y_bar <= (y + h))):
                                    matchedFid = fid

                            # 如果当前检测到的人脸是陌生人脸且未被跟踪
                            if not isKnown and matchedFid is None:
                                # 创建一个人脸跟踪器
                                tracker = dlib.correlation_tracker()
                                # 锁定跟踪范围
                                tracker.start_track(realTimeFrame, dlib.rectangle(x - 5, y - 10, x + w + 5, y + h + 10))
                                # 将该人脸跟踪器分配给当前检测到的人脸
                                faceTrackers[currentFaceID] = tracker
                                # 人脸ID自增
                                currentFaceID += 1

                    # 使用当前的人脸跟踪器，更新画面，输出跟踪结果
                    for fid in faceTrackers.keys():
                        tracked_position = faceTrackers[fid].get_position()

                        t_x = int(tracked_position.left())
                        t_y = int(tracked_position.top())
                        t_w = int(tracked_position.width())
                        t_h = int(tracked_position.height())

                        # 在跟踪帧中圈出人脸
                        cv2.rectangle(realTimeFrame, (t_x, t_y), (t_x + t_w, t_y + t_h), (0, 0, 255), 2)
                        cv2.putText(realTimeFrame, 'tracking...', (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),
                                    2)

                captureData['originFrame'] = frame
                captureData['realTimeFrame'] = realTimeFrame
                self.captureQueue.put(captureData)

            else:
                continue

    # 停止OpenCV线程
    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()
