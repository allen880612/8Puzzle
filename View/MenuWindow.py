# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Model import DataModel as DM

class Menu(object):
    def __init__(self, data):
        self._isStart = False
        self.isOpen = False
        self.data = data

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lableGameLogo = QtWidgets.QLabel(self.centralwidget)
        self.lableGameLogo.setGeometry(QtCore.QRect(20, 20, 350, 250))
        self.lableGameLogo.setObjectName("lableGameLogo")
        self.textBoxPuzzleSize = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBoxPuzzleSize.setGeometry(QtCore.QRect(220, 390, 101, 31))
        self.textBoxPuzzleSize.setObjectName("textBoxPuzzleSize")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(360, 320, 230, 100))
        self.buttonStart.setObjectName("buttonStart")
        self.buttonImportImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImportImage.setGeometry(QtCore.QRect(510, 250, 81, 31))
        self.buttonImportImage.setObjectName("buttonImportImage")
        self.labelPreviewImage = QtWidgets.QLabel(self.centralwidget)
        self.labelPreviewImage.setGeometry(QtCore.QRect(420, 50, 180, 180))
        self.labelPreviewImage.setObjectName("labelPreviewImage")
        self.labelTip = QtWidgets.QLabel(self.centralwidget)
        self.labelTip.setGeometry(QtCore.QRect(20, 400, 161, 21))
        self.labelTip.setObjectName("labelTip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu8_Puzzle_Initilize = QtWidgets.QMenu(self.menubar)
        self.menu8_Puzzle_Initilize.setObjectName("menu8_Puzzle_Initilize")
        self.menuRecord = QtWidgets.QMenu(self.menubar)
        self.menuRecord.setObjectName("menuRecord")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu8_Puzzle_Initilize.menuAction())
        self.menubar.addAction(self.menuRecord.menuAction())

        #  自定義功能區
        self.buttonStart.clicked.connect(self.Start)
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lableGameLogo.setText(_translate("MainWindow", "Game cover image"))
        self.buttonStart.setText(_translate("MainWindow", "開始遊戲"))
        self.buttonImportImage.setText(_translate("MainWindow", "匯入圖片"))
        self.labelPreviewImage.setText(_translate("MainWindow", "Preview of image"))
        self.labelTip.setText(_translate("MainWindow", "請輸入圖片切成一列有幾張"))
        self.menu8_Puzzle_Initilize.setTitle(_translate("MainWindow", "File"))
        self.menuRecord.setTitle(_translate("MainWindow", "Record"))

    def IsStart(self):
        return self._isStart

    def Start(self):
        self._isStart = True
        self.data.SetButtonCount(5)



