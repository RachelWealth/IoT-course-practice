# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1207, 893)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(140, 16777215))
        self.scrollArea.setStyleSheet("background-color:rgb(1,22,39);\n"
"color:white;\n"
"border-top:1px solid white;\n"
"border-bottom:1px solid white;\n"
"border-left:1px solid white;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 138, 816))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 101, 655))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_manager = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_manager.setStyleSheet("border:none;\n"
"color:white;")
        self.button_manager.setObjectName("button_manager")
        self.horizontalLayout.addWidget(self.button_manager)
        self.buttonAddObject = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonAddObject.setStyleSheet("border:none;\n"
"color:white;\n"
"font: 7pt \"AcadEref\";")
        self.buttonAddObject.setObjectName("buttonAddObject")
        self.horizontalLayout.addWidget(self.buttonAddObject)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(".QListWidget{\n"
"    background-color: rgb(55,55,55);\n"
"    border-radius:10px;\n"
"    padding:5px;\n"
"    border:none;\n"
"    height: 200;\n"
"}\n"
".QListWidget::Item{\n"
"    font: 10pt \"仿宋\";\n"
"    color:white;\n"
"    font-weight:bold;\n"
"}")
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setGridSize(QtCore.QSize(0, 30))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_manager_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_manager_2.setStyleSheet("border:none;\n"
"color:white;")
        self.button_manager_2.setObjectName("button_manager_2")
        self.horizontalLayout_2.addWidget(self.button_manager_2)
        self.button_add_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_add_2.setStyleSheet("border:none;\n"
"color:white;\n"
"font: 7pt \"AcadEref\";")
        self.button_add_2.setText("")
        self.button_add_2.setObjectName("button_add_2")
        self.horizontalLayout_2.addWidget(self.button_add_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidget_2.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("仿宋 white")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(55,55,55);\n"
"font: 10pt \"仿宋\" white;\n"
"border-radius:10px;\n"
"padding:5px;\n"
"border:none;")
        self.listWidget_2.setGridSize(QtCore.QSize(0, 30))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        self.verticalLayout.addWidget(self.listWidget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setStyleSheet("background-color:rgb(1,22,39);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setToolTip("")
        self.tableWidget.setStyleSheet(".QTableWidget::Item{\n"
"    color:#6FD3CA;\n"
"    \n"
"}\n"
".QTableWidget{\n"
"    border:none;\n"
"}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3.addWidget(self.splitter)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setStyleSheet("background-color:rgb(1,22,39);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.labelLogin = QtWidgets.QLabel(self.groupBox_3)
        self.labelLogin.setGeometry(QtCore.QRect(10, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelLogin.setFont(font)
        self.labelLogin.setStyleSheet("color:white;\n"
"font: 14pt \"宋体\";")
        self.labelLogin.setObjectName("labelLogin")
        self.labelBirthday = QtWidgets.QLabel(self.groupBox_3)
        self.labelBirthday.setGeometry(QtCore.QRect(20, 90, 51, 41))
        self.labelBirthday.setStyleSheet("font: 10pt \"宋体\";\n"
"color:white;\n"
"")
        self.labelBirthday.setText("")
        self.labelBirthday.setObjectName("labelBirthday")
        self.labelID = QtWidgets.QLabel(self.groupBox_3)
        self.labelID.setGeometry(QtCore.QRect(20, 140, 51, 41))
        self.labelID.setStyleSheet("font: 10pt \"宋体\";\n"
"color:white;\n"
"")
        self.labelID.setText("")
        self.labelID.setObjectName("labelID")
        self.labelAddMeber = QtWidgets.QLabel(self.groupBox_3)
        self.labelAddMeber.setGeometry(QtCore.QRect(110, 50, 51, 16))
        self.labelAddMeber.setStyleSheet("color:white;")
        self.labelAddMeber.setObjectName("labelAddMeber")
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1207, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actionlianjie = QtWidgets.QAction(MainWindow)
        self.actionlianjie.setObjectName("actionlianjie")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menu.addAction(self.actionlianjie)
        self.menu_2.addAction(self.actionabout)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "家庭管家系统"))
        self.button_manager.setText(_translate("MainWindow", "管理"))
        self.buttonAddObject.setText(_translate("MainWindow", "添加"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "衣服"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "调料"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "图书"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.button_manager_2.setText(_translate("MainWindow", "管理"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "颜色"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "品牌"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "季节"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "红色"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "绿色"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "黄色"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "蓝色"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "粉色"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "橙色"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "白色"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "黑色"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "灰色"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.labelLogin.setText(_translate("MainWindow", "登录"))
        self.labelAddMeber.setText(_translate("MainWindow", "添加"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionlianjie.setText(_translate("MainWindow", "连接"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
