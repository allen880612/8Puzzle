from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from View import UI

from Controller import RandomPuzzle as RP

class PreGaming(QMainWindow):
    def __init__(self, data):
        super(PreGaming, self).__init__()
        self.ui = UI.Ui_PreGaming()
        self.ui.setupUi(self)
        self.SetUI()
        self.data = data
        #self.signal = DM.Signal()
        self.data.dataSignal.signal.connect(self.ReviceMessage)
        self.buttonList = []
        self.puzzle = None
        self.puzzleControl = None

    def SetUI(self):
        self.ui.labelHint.adjustSize()  # QLabel 自適應大小
        self.ui.buttonDynamic.setVisible(False)

    def ReviceMessage(self, message):
        if message == "Goto2":
            print("Revice! " + message)
            colNum = self.data.GetButtonCount()
            self.AddButtonList(colNum)
            self.puzzleControl = RP.RandomMatrix(colNum)

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
        newButton = QtWidgets.QPushButton(self.ui.centralwidget)
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
        newButton = QtWidgets.QPushButton(self.ui.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))
        newButton.setFlat(True)

        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        newButton.setStyleSheet("border-image: url(subImage/" + str(buttonIndex) + ".png);")

        return newButton

    def ClearButton(self):
        for rowBtn in self.buttonList:
            for btn in rowBtn:
                btn.deleteLater()
        self.buttonList.clear()

    def ClickButton(self, buttonIndex):
        self.ui.buttonDynamic.click()
        print(buttonIndex)
        self.puzzleControl.ResetPuzzleBlankLocation(buttonIndex)  # 依按下位置，改變亂數產生之puzzle
        self.data.SetPuzzle(self.puzzleControl.GetPuzzle())
        self.data.SetNowNullButtonIndex(buttonIndex)
        self.data.dataSignal.Shoot("Goto3")

