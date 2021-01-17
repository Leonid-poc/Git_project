# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(33, 68, 207, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 255);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label_3.setLineWidth(1)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(0, 255, 255);")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.label_6.setLineWidth(1)
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "скин_1"))
        self.pushButton_3.setText(_translate("MainWindow", "скин_3"))
        self.pushButton_2.setText(_translate("MainWindow", "скин_2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Скины"))
        self.pushButton_6.setText(_translate("MainWindow", "Пустыня"))
        self.pushButton_4.setText(_translate("MainWindow", "Джунгли"))
        self.pushButton_5.setText(_translate("MainWindow", "Зима"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Уровни"))