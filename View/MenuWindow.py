from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PIL import Image
from PyQt5.QtWidgets import QMainWindow
from Controller import FileDialog as FD
from Controller import ImageControl as IMG_CONTROL
from Controller import FuntionTools
from View import UI

class Menu(QMainWindow):
    def __init__(self, _data):
        super(Menu, self).__init__()
        self._isStart = False
        self.isOpen = False
        self.data = _data
        self.fileDialog = FD.FileControl()
        self.imgCtrl = IMG_CONTROL.ImageControl(_data)
        #self.signal = DM.Signal()
        self.ui = UI.Ui_Menu()
        self.ui.setupUi(self)


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
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        # self.buttonLoad.objectName = "buttonLoad"
        # self.buttonLoad.setGeometry(QtCore.QRect(20, 300, 50, 50))
        # self.buttonLoad.setText("讀檔")
        # self.buttonLoad.setFont(font)
        self.ui.buttonLoad.adjustSize()
        self.ui.buttonLoad.clicked.connect(self.ClickLoadButton)
        self.ui.buttonLoad.setVisible(True)
        #  Cover
        self.ui.lableGameLogo.setPixmap(QPixmap("Image/Cover.png"))
        self.ui.lableGameLogo.setAutoFillBackground(True)

        #  自定義功能區
        self.ui.buttonStart.clicked.connect(self.Start)
        self.ui.buttonImportImage.clicked.connect(self.ImportImage)
        self.ui.labelPreviewImage.setScaledContents(True)  # 圖片能符合label大小ˋ

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
        matrixSize = self.GetInputNumber(self.ui.textBoxPuzzleSize.toPlainText())
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
                self.ui.labelPreviewImage.setPixmap(self.data.GetPixmap())
        else:
            print("取消選擇圖片")


    def GetInputNumber(self, inputString):
        try:
            return int(inputString)
        except:
            return 3
