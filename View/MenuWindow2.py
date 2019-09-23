from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Menu(QMainWindow):

    def __init__(self):
        self._isStart = False
        self.isOpen = False
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menu8_Puzzle_Initilize = QtWidgets.QMenu(self.menubar)
        self.menu8_Puzzle_Initilize.setObjectName("menu8_Puzzle_Initilize")
        self.menuRecord = QtWidgets.QMenu(self.menubar)
        self.menuRecord.setObjectName("menuRecord")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu8_Puzzle_Initilize.menuAction())
        self.menubar.addAction(self.menuRecord.menuAction())

        #  自定義功能區
        self.buttonStart.clicked.connect(self.Start)
        #
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "233"))
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

