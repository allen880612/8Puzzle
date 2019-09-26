from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Controller import RandomPuzzle as RP

class PreGamingWindow(object):
    def __init__(self, data):
        self.data = data
        #self.signal = DM.Signal()
        self.data.dataSignal.signal.connect(self.ReviceMessage)
        self.buttonList = []
        self.puzzle = None
        self.puzzleControl = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonDynamic = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDynamic.setObjectName("buttonDynamic")
        self.gridLayout.addWidget(self.buttonDynamic, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.labelHint = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelHint.setFont(font)
        self.labelHint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelHint.setWordWrap(False)
        self.labelHint.setObjectName("labelHint")
        self.gridLayout_2.addWidget(self.labelHint, 2, 1, 1, 1)
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBack.setFont(font)
        self.buttonBack.setObjectName("buttonBack")
        self.gridLayout_2.addWidget(self.buttonBack, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonDynamic.setText(_translate("MainWindow", "PushButton"))
        self.labelHint.setText(_translate("MainWindow", "點擊任意一格來開始遊戲!"))
        self.buttonBack.setText(_translate("MainWindow", "Back"))
        self.labelHint.adjustSize(); #QLabel 自適應大小
        self.buttonDynamic.setVisible(False)

    def ReviceMessage(self, message):
        if message == "Goto2":
            print("Revice! " + message)
            colNum = self.data.GetButtonCount()
            self.AddButtonList(colNum)
            self.puzzleControl = RP.RandomMatrix(self.data, colNum)

    def AddButtonList(self, addRowButtonCount):
        totalButtonCount = addRowButtonCount ** 2
        self.ClearButton()
        pixmapList = self.data.GetPixmapList()
        for i in range(addRowButtonCount):
            rowButtonList = []
            for j in range(addRowButtonCount):
                buttonIndex = i * addRowButtonCount + j
                if pixmapList:  # test 用
                    rowButtonList.append(self.AddButton(j, i, buttonIndex, pixmapList[buttonIndex]))
                else:
                    rowButtonList.append(self.AddButton2(j, i, buttonIndex))

            self.buttonList.append(rowButtonList)

    #test - no image
    def AddButton2(self, row, column, buttonIndex):
        size = 100
        dButtonPos = (100, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))
        return newButton

    def AddButton(self, row, column, buttonIndex, pixmap):
        size = 100
        dButtonPos = (100, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))
        newButton.setFlat(True)

        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        newButton.setStyleSheet("border-image: url(subImage/" + str(buttonIndex) + ".jpg);")

        return newButton

    def ClearButton(self):
        for rowBtn in self.buttonList:
            for btn in rowBtn:
                btn.deleteLater()
        self.buttonList.clear()

    def ClickButton(self, buttonIndex):
        self.buttonDynamic.click()
        print(buttonIndex)
        self.puzzleControl.ResetPuzzleBlankLocation(buttonIndex)  # 依按下位置，改變亂數產生之puzzle
        #self.data.SetNowNullButtonIndex(buttonIndex)
        self.data.dataSignal.Shoot("Goto3")


