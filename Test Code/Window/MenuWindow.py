import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow


class TestUI(object):
    def __init__(self):
        self._isStart = False
        self.isOpen = False

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
        self.buttonImportImage.clicked.connect(self.ImportImage)
        self.labelPreviewImage.setScaledContents(True)  #  圖片能符合label大小ˋ

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.UISetting(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8 Puzzle !"))
        self.lableGameLogo.setText(_translate("MainWindow", "Game cover image"))
        self.buttonStart.setText(_translate("MainWindow", "開始遊戲"))
        self.buttonImportImage.setText(_translate("MainWindow", "匯入圖片"))
        self.labelPreviewImage.setText(_translate("MainWindow", "Preview of image"))
        self.labelTip.setText(_translate("MainWindow", "請輸入圖片切成一列有幾張"))
        self.menu8_Puzzle_Initilize.setTitle(_translate("MainWindow", "File"))
        self.menuRecord.setTitle(_translate("MainWindow", "Record"))


    def UISetting(self, MainWindow):
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.objectName = "buttonLoad"
        self.buttonLoad.setGeometry(QtCore.QRect(20, 300, 50, 50))
        self.buttonLoad.setText("讀檔")
        self.buttonLoad.setFont(font)
        self.buttonLoad.adjustSize()
        self.buttonLoad.clicked.connect(self.ClickLoadButton)
        self.buttonLoad.setVisible(True)

        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        # Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        MainWindow.setPalette(pe)
        MainWindow.setWindowIcon(QIcon("image/icon.png"))


    def ClickLoadButton(self):
        message = "Goto3"
        print("Click load")

    def IsStart(self):
        return self._isStart

    def Start(self):
        message = "Goto2"
        matrixSize = self.GetInputNumber(self.textBoxPuzzleSize.toPlainText())
        self._isStart = True
        print("Shoot!" + message + "\nsize: " + str(matrixSize))


    def ImportImage(self):
        #  強迫要選到圖
        while True:
            selectImage = self.fileDialog.openFileNameDialog()
            print("開啟圖片 : " + str(selectImage))
            if selectImage:
                break

    def GetInputNumber(self, inputString):
        try:
            return int(inputString)
        except:
            return 3



app = QApplication(sys.argv)


mainWindow = QMainWindow()
testWindow = TestUI()
testWindow.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())


# myMainWindow = QMainWindow()
# myUi = TestUI()
# myUi.setupUi(myMainWindow)
# myMainWindow.show()
#
# sys.exit(app.exec_())