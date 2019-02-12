# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'narcelik.ui',
# licensing of 'narcelik.ui' applies.
#
# Created: Tue Feb 12 18:02:58 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 326)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":root/narcelik.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 60))
        self.lcdNumber.setProperty("value", 23.59)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "PROG", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "AUTO", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "HOUR", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "MIN", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("Form", "AROMA", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("Form", "⏻", None, -1))

import narcelik_rc
