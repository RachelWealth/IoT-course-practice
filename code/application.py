from managerUI import MainUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
import threading
from PyQt5.QtCore import QTimer, pyqtSlot, QStringListModel
from managerSQL import managerSQL
import logging
from Serial import Serial
from WarningQDialog import WarningQDialog
from classfier import classfier

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

sqlDic = {2: 'cloth', 3: 'flavoring', 4: 'book'}


class AppWindow(QMainWindow, MainUi):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        self.result = []
        self.queryTableName = ''  # the name of table we need to query
        self.sqlHelper = managerSQL()
        self.classHelper = classfier()

        self._timer.timeout.connect(self.voiceManager)
        self._timer.start(1000)  # plot after 1s delay

    @pyqtSlot()
    def on_label_cloth_click(self):
        self.__searchHelper__('cloth')
        self.__subClassDisplay__('cloth')

    @pyqtSlot()
    def on_label_flavoring_click(self):
        self.__searchHelper__('flavoring')
        self.__subClassDisplay__('flavoring')

    @pyqtSlot()
    def on_label_book_click(self):
        self.__searchHelper__('book')
        self.__subClassDisplay__('book')

    @pyqtSlot()
    def on_button_color_click(self):
        self.showMyObject(self)

    @pyqtSlot()
    def on_button_cbranch_click(self):

    @pyqtSlot()
    def on_button_season_click(self):

    @pyqtSlot()
    def on_button_fbrand_click(self):


    def __searchHelper__(self, tableName):
        """
        search the object by its type
        :param tableName: the same with type name
        :return: self.result
        """
        logging.info("search from " + tableName + '...')
        self.queryTableName = tableName
        self.sqlHelper.executeQuery1(tableName)

    def __subClassDisplay__(self,objName):
        """
        this function to dispaly the subclass list of every type of object
        :param objName: value:cloth, flavoring, book and so on
        :return:
        """
        slm = QStringListModel()
        self.currentObject = objName
        self.myList = list(self.classHelper.home.get(objName))
        slm.setStringList(self.myList)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.subClassRes)
        layout.addWidget(self.listView)
        self.setLayout(layout)

    def subClassRes(self, qModelIndex):
        """
        click feature area to get more detailed classfier
        :return:
        """
        if self.currentObject == 'cloth':
            self.rightClass = list(self.classHelper.homeCloth.get(self.myList[qModelIndex.row()]))
        elif self.currentObject == 'flavoring':
            self.rightClass = list(self.classHelper.homeFlavoring.get(self.myList[qModelIndex.row()]))
        elif self.currentObject == 'book':
            self.rightClass = list(self.classHelper.homeBook.get(self.myList[qModelIndex.row()]))
        self.rightFieldShow()

    def rightFieldShow(self):
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

    
