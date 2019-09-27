from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PIL import Image
from Controller import FileDialog as FD
from Controller import ImageControl as IMG_CONTROL
from Controller import FuntionTools
class Menu(object):
    def __init__(self, _data):
        self._isStart = False
        self.isOpen = False
        self.data = _data
        self.fileDialog = FD.FileControl()
        self.imgCtrl = IMG_CONTROL.ImageControl(_data)
        #self.signal = DM.Signal()

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



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.UISetting()

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


    def UISetting(self):
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
        #  Cover
        self.lableGameLogo.setPixmap(QPixmap("Image/Cover.png"))
        self.lableGameLogo.setAutoFillBackground(True)

        #  自定義功能區
        self.buttonStart.clicked.connect(self.Start)
        self.buttonImportImage.clicked.connect(self.ImportImage)
        self.labelPreviewImage.setScaledContents(True)  # 圖片能符合label大小ˋ

    def ClickLoadButton(self):
        message = "Goto3"
        dataDict = FuntionTools.readJson("data.json")
        self.data.SetData(dataDict)
        self.data.SetPuzzle(dataDict["puzzle"])
        self.data.SetButtonCount(dataDict["rowButtonCount"])
        #self.data.SetPixmapList(dataDict["pixmapList"])
        self.data.SetImagePath(dataDict["imagePath"])
        if self.data.GetImagePath():
            self.imgCtrl.LoadImage(self.data.GetImagePath())
        self.imgCtrl.SetImageList(self.data.GetButtonCount())
        print("Click load")
        self.data.dataSignal.Shoot(message)

    def IsStart(self):
        return self._isStart

    def Start(self):
        message = "Goto2"
        matrixSize = self.GetInputNumber(self.textBoxPuzzleSize.toPlainText())
        self._isStart = True
        self.data.SetButtonCount(matrixSize)
        print("Shoot!" + message + "\nsize: " + str(matrixSize))
        try: #小防呆
            self.imgCtrl.SetImageList(matrixSize)
        except:
            pass
        self.data.dataSignal.Shoot(message)

    def ImportImage(self):

        selectImage = self.fileDialog.openFileNameDialog()
        print("開啟圖片 : " + str(selectImage))
        # 有選擇圖片
        if selectImage:
            self.imgCtrl.LoadImage(selectImage)
            # 確認Load的是圖片
            if self.imgCtrl.isloaded:
                self.data.SetImagePath(selectImage)
                self.labelPreviewImage.setPixmap(self.data.GetPixmap())
        else:
            print("取消選擇圖片")


    def GetInputNumber(self, inputString):
        try:
            return int(inputString)
        except:
            return 3
