# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 448)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 511, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(100, 60, 91, 41))
        self.label.setStyleSheet("font: 14pt \"宋体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 91, 41))
        self.label_2.setStyleSheet("font: 14pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.inputUserName = QtWidgets.QLineEdit(self.tab)
        self.inputUserName.setGeometry(QtCore.QRect(210, 60, 181, 31))
        self.inputUserName.setObjectName("inputUserName")
        self.inputPwd = QtWidgets.QLineEdit(self.tab)
        self.inputPwd.setGeometry(QtCore.QRect(210, 130, 181, 31))
        self.inputPwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.inputPwd.setObjectName("inputPwd")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(320, 250, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 491, 341))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.checkBoxUseExterCam = QtWidgets.QCheckBox(self.tab_2)
        self.checkBoxUseExterCam.setGeometry(QtCore.QRect(10, 360, 131, 40))
        self.checkBoxUseExterCam.setObjectName("checkBoxUseExterCam")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.label_3.setText(_translate("Dialog", "请开启摄像头"))
        self.checkBoxUseExterCam.setText(_translate("Dialog", "使用外接摄像头"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
