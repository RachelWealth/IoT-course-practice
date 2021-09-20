from managerUI import MainUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
import threading
from PyQt5.QtCore import QTimer, pyqtSlot
from managerSQL import managerSQL
import logging
from Serial import Serial
from WarningQDialog import WarningQDialog

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

        self._timer.timeout.connect(self.voiceManager)
        self._timer.start(1000)  # plot after 1s delay

    @pyqtSlot()
    def on_label_cloth_click(self):
        self.__searchHelper__('cloth')

    @pyqtSlot()
    def on_left_label_2_click(self):
        self.__searchHelper__('flavoring')

    @pyqtSlot()
    def on_left_label_3_click(self):
        self.__searchHelper__('book')

    def __searchHelper__(self, tableName):
        """
        search the object by its type
        :param tableName: the same with type name
        :return: self.result
        """
        logging.info("search from " + tableName + '...')
        self.queryTableName = tableName
        self.sqlHelper.executeQuery1(tableName)

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

    def showMyObject(self):
        """
        Show the object we have in the right side
        :return:
        """
        
