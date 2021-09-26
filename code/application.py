from managerUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
import threading
from PyQt5.QtCore import QTimer, QUrl
from managerSQL import managerSQL
import logging
from Serial import Serial
from WarningQDialog import WarningQDialog
from classifier import classifier
from PyQt5.QtWebEngineWidgets import *

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

sqlDic = {2: 'cloth', 3: 'flavoring', 4: 'book'}

global TABLE_MAX_COL
TABLE_MAX_COL = 6


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.result = []
        self.queryTableName = ''  # the name of table we need to query
        self.sqlHelper = managerSQL()
        self.classHelper = classifier()
        self.firstClass = ''
        self.secondClass = ''
        self.thirdClass = ''

        print('---------------set timeer---------------')
        logging.info('---------------set timeer---------------')
        self._timer = QTimer(self)
        # self._timer.timeout.connect(self.__voiceManager__)
        self._timer.start(1000)  # plot after 1s delay

        print('---------------set list item response action---------------')
        logging.info('---------------set list item response action---------------')
        # first class list clicked response
        self.listWidget.itemClicked.connect(self.__firstClassClick__)
        # second class list clicked response
        self.listWidget_2.itemClicked.connect(self.__secondClassClick__)
        # third class list clicked response
        self.tableWidget.itemClicked.connect(self.__thirdClassClick__)

        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('https://www.baidu.com'))
        # self.setCentralWidget(self.browser)
        self.grid = QGridLayout(self.groupBox_2)
        self.grid.addWidget(self.browser)

        print("finish initial")
        logging.info("finish initial")

    def __firstClassClick__(self):
        logging.info('------------------------------')
        num = self.listWidget.selectedIndexes()[0].row()
        print('__objectClick__'+str(num))
        self.firstClass = self.classHelper.homeObj.get(num)
        logging.info('click '+self.firstClass+'item')
        print('click '+self.firstClass+' item')
        self.__searchHelper__(self.firstClass)
        self.__subClassDisplay__(num)

    def __searchHelper__(self, tableName):
        """
        search the object by its type
        :param tableName: the same with type name
        :return: self.result
        """
        logging.info("search from " + tableName + '...')
        print("search from " + tableName + '...')
        self.queryTableName = tableName
        self.sqlHelper.executeQuery1(tableName)

    def __subClassDisplay__(self, num):
        """
        this function to dispaly the second class list of every type of object
        :param onum: value:cloth-0, flavoring-1, book-2 and so on
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
        if self.currentObject == 'cloth':
            self.rightClass = list(self.classHelper.homeCloth.get(self.myList[qModelIndex.row()]))
        elif self.currentObject == 'flavoring':
            self.rightClass = list(self.classHelper.homeFlavoring.get(self.myList[qModelIndex.row()]))
        elif self.currentObject == 'book':
            self.rightClass = list(self.classHelper.homeBook.get(self.myList[qModelIndex.row()]))
        self.__rightThirdClassShow__()

    def __rightThirdClassShow__(self):
        """
        display of third class classifier
        :return:
        """
        self.tableWidget.clear()
        i = 0
        col = 0
        row = 0
        for itemName in self.rightClass:
            if col < TABLE_MAX_COL:
                item = self.tableWidget.item(col, row)
                _translate = QtCore.QCoreApplication.translate
                item.setText(_translate("MainWindow", itemName))
                col += 1
            elif col == TABLE_MAX_COL and row < 1:
                col = 0
                row += 1
                item = self.tableWidget.item(col, row)
                _translate = QtCore.QCoreApplication.translate
                item.setText(_translate("MainWindow", itemName))
            elif col == TABLE_MAX_COL and row == 1:
                item = QtWidgets.QTableWidgetItem(itemName)
                self.tableWidget.setItem(row, col, item)

    def __thirdClassClick__(self,qTableIndex):
        self.thirdClass = self.tableWidget.item(qTableIndex.row(),qTableIndex.column()).text()
        logging.info('third class click:' + self.thirdClass)
        self.objSet = self.sqlHelper.executeQuery2(self.firstClass,self.secondClass,self.thirdClass)
        self.__objFieldShow__()

    def __objFieldShow__(self):
        """
        this function used to switch the display content
        :return:
        """


    def __subSearchHelper__(self, tableName, subClass, reSubClass):
        """

        :param tableName: the same with type name
        :param subClass: the detailed class of the object
        :param reSubClass: the class of subClass
        :return:
        """

    def __voiceManager__(self):
        """
        To process the voice command we get from serial
        :return:
        """
        self.serial = Serial()
        self.port = self.serial.getSerial()
        command = self.serial.readSerial()
        if sqlDic.get(command) is not None:
            self.sqlHelper.executeQuery1(sqlDic[command])
        elif command == 0:
            # add some process to show this action
            pass
        elif command == -1:
            WarningQDialog("Sorry, I can't recognize your command")
        else:
            pass
