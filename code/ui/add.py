# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 452)
        Dialog.setStyleSheet("background-color:rgb(40, 41, 35);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 390, 281, 32))
        self.buttonBox.setStyleSheet("color:rgb(255, 255, 255)")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 40, 141, 22))
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:#282923;\n"
"border-radius:5px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 81, 21))
        self.label.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
"color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 81, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
"color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 100, 141, 22))
        self.comboBox_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:#282923;\n"
"border-radius:5px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 160, 141, 22))
        self.comboBox_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:#282923;\n"
"border-radius:5px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 81, 21))
        self.label_3.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
"color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 220, 141, 22))
        self.comboBox_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:#282923;\n"
"border-radius:5px;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 81, 21))
        self.label_4.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
"color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(70, 280, 261, 81))
        self.textEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "衣服"))
        self.comboBox.setItemText(1, _translate("Dialog", "调料"))
        self.comboBox.setItemText(2, _translate("Dialog", "图书"))
        self.label.setText(_translate("Dialog", "物品"))
        self.label_2.setText(_translate("Dialog", "颜色"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "红"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "绿"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "黄"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "蓝"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "粉"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "橙"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "白"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "黑"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "灰"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Veromoda"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "LEDIN"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "OLNY"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "ANTA"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "SEMIR"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "Teek"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "特步"))
        self.label_3.setText(_translate("Dialog", "品牌"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "春"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "夏"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "秋"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "冬"))
        self.label_4.setText(_translate("Dialog", "季节"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "请拖入物品图片"))
