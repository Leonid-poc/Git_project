# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow_1):
        MainWindow_1.setObjectName("MainWindow_1")
        MainWindow_1.resize(764, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow_1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 25.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMaximum(101)
        self.horizontalSlider.setProperty("value", 25)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setMaximum(101)
        self.horizontalSlider_2.setProperty("value", 25)
        self.horizontalSlider_2.setTracking(True)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_3.addWidget(self.horizontalSlider_2, 2, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setMidLineWidth(0)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("value", 25.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_3.addWidget(self.lcdNumber_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        MainWindow_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_1)
        self.statusbar.setObjectName("statusbar")
        MainWindow_1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)

    def retranslateUi(self, MainWindow_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_1.setWindowTitle(_translate("MainWindow_1", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow_1", "Звук музыки:"))
        self.groupBox_2.setTitle(_translate("MainWindow_1", "Зввуки эффектов:"))
