# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lableGameLogo = QtWidgets.QLabel(self.centralwidget)
        self.lableGameLogo.setGeometry(QtCore.QRect(40, 30, 320, 320))
        self.lableGameLogo.setObjectName("lableGameLogo")
        self.textBoxPuzzleSize = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBoxPuzzleSize.setGeometry(QtCore.QRect(150, 400, 101, 31))
        self.textBoxPuzzleSize.setObjectName("textBoxPuzzleSize")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(460, 390, 157, 56))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.buttonStart.setFont(font)
        self.buttonStart.setObjectName("buttonStart")
        self.buttonImportImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImportImage.setGeometry(QtCore.QRect(510, 300, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonImportImage.setFont(font)
        self.buttonImportImage.setObjectName("buttonImportImage")
        self.labelPreviewImage = QtWidgets.QLabel(self.centralwidget)
        self.labelPreviewImage.setGeometry(QtCore.QRect(410, 100, 180, 180))
        self.labelPreviewImage.setObjectName("labelPreviewImage")
        self.labelTip = QtWidgets.QLabel(self.centralwidget)
        self.labelTip.setGeometry(QtCore.QRect(40, 400, 93, 26))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTip.setFont(font)
        self.labelTip.setObjectName("labelTip")
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.setGeometry(QtCore.QRect(290, 390, 157, 56))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad.setFont(font)
        self.buttonLoad.setObjectName("buttonLoad")
        self.labelTip_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelTip_2.setGeometry(QtCore.QRect(410, 50, 63, 26))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelTip_2.setFont(font)
        self.labelTip_2.setObjectName("labelTip_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lableGameLogo.setText(_translate("MainWindow", "Game cover image"))
        self.buttonStart.setText(_translate("MainWindow", "開始遊戲"))
        self.buttonImportImage.setText(_translate("MainWindow", "匯入圖片"))
        self.labelPreviewImage.setText(_translate("MainWindow", "Preview of image"))
        self.labelTip.setText(_translate("MainWindow", "列/欄數："))
        self.buttonLoad.setText(_translate("MainWindow", "繼續遊戲"))
        self.labelTip_2.setText(_translate("MainWindow", "預覽："))
