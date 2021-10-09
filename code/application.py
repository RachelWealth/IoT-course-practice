import json
import sys
import threading

from IoTPractice.code.add import add_Dialog
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

        self.buttonAddObject.clicked.connect(self.__addObject__)
        # self.buttonAddObject.clicked.connect(add_Dialog.show)
        # self.button_add.clicked(self.addObject)

        self.actionlianjie.triggered.connect(self.__connectSerial__)
        # self.action_4.triggered.connect(self.__connectAbout__)

        self.browser = QWebEngineView()
        # self.browser.load(QUrl('file:///E:/workplace/pycharmWork/IoTPractice/IoTPractice/code/web/templates/welcom.html'))
        self.browser.load(
            QUrl(r'http://localhost:5000/welcom'))
        self.grid = QGridLayout(self.groupBox_2)
        self.grid.addWidget(self.browser)
        self.fileHelper = sendDataHelper()

        print("finish initial")
        logging.info("finish initial")

    def __getRighrtAndSecondClass__(self,firstClass=None):
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


    def __addObject__(self):
        dia = QtWidgets.QDialog()
        addWin = add_Dialog()
        addWin.setupUi(dia)
        if dia.exec():      # click OK
            print(1)
        else:               # click CANCEL
            pass

    # def __addMember__(self):




