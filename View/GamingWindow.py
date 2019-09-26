from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Controller import RandomPuzzle
from Controller import FuntionTools
from Controller import PuzzleAlgorithm as PA
import threading
import json

class GameWindow(object):
    def __init__(self, data):
        self.data = data
        self.data.dataSignal.signal.connect(self.ReviceMessage)
        self.puzzle = [] #add
        self.buttonList = [] #add

        self.puzzlePath = None
        self.step = 0 # now step
        self.totalStep = 0 # 演算法總共要走的步數
        self.movePath = None # 每步的移動
        self.nullBtnIndexRow, self.nullBtnIndexCol = 0, 0 #目前的空按鈕位置

    def ReviceMessage(self, message):
        return False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 401, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonAutoFinish = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAutoFinish.setGeometry(QtCore.QRect(440, 100, 183, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonAutoFinish.setFont(font)
        self.buttonAutoFinish.setObjectName("buttonAutoFinish")
        self.labelStep = QtWidgets.QLabel(self.centralwidget)
        self.labelStep.setGeometry(QtCore.QRect(330, 380, 248, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelStep.setFont(font)
        self.labelStep.setObjectName("labelStep")
        self.buttonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNextStep.setGeometry(QtCore.QRect(440, 160, 183, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonNextStep.setFont(font)
        self.buttonNextStep.setObjectName("buttonNextStep")
        self.labelHelp = QtWidgets.QLabel(self.centralwidget)
        self.labelHelp.setGeometry(QtCore.QRect(480, 10, 80, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelHelp.setFont(font)
        self.labelHelp.setObjectName("labelHelp")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(20, 380, 93, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.buttonRestart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRestart.setGeometry(QtCore.QRect(140, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRestart.setFont(font)
        self.buttonRestart.setObjectName("buttonRestart")
        self.buttonMenu = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMenu.setGeometry(QtCore.QRect(440, 300, 108, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMenu.setFont(font)
        self.buttonMenu.setObjectName("buttonMenu")
        self.buttonNextStep_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNextStep_2.setGeometry(QtCore.QRect(440, 230, 183, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonNextStep_2.setFont(font)
        self.buttonNextStep_2.setObjectName("buttonNextStep_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.buttonNextStep.clicked.connect(self.AI_NextStep)
        self.buttonAutoFinish.clicked.connect(lambda: self.AI_AutoComplete(0.05))
        self.retranslateUi(MainWindow)

        self.UISetting()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonAutoFinish.setText(_translate("MainWindow", "AI 自動完成"))
        self.labelStep.setText(_translate("MainWindow", "已用步數：0"))
        self.buttonNextStep.setText(_translate("MainWindow", "AI 解下一步"))
        self.labelHelp.setText(_translate("MainWindow", "幫助"))
        self.buttonSave.setText(_translate("MainWindow", "存檔"))
        self.buttonRestart.setText(_translate("MainWindow", "重新開始"))
        self.buttonMenu.setText(_translate("MainWindow", "回選單"))
        self.buttonNextStep_2.setText(_translate("MainWindow", "演算法下一步"))

    def UISetting(self):
        self.buttonSave.clicked.connect(self.ClickSaveButton)

    # Add
    def ReviceMessage(self, message):
        if message == "Goto3":
            print("Revice! " + message)
            self.CreateRandomPuzzle()

    #Add connect
    def AI_NextStep(self):
        #print(self.nullBtnIndexRow, self.nullBtnIndexCol)
        self.nullBtnIndexRow, self.nullBtnIndexCol = self.MoveButton(self.nullBtnIndexRow, self.nullBtnIndexCol, self.movePath[self.step])
        self.UpdateButtonPosition()
        #QtWidgets.QApplication.processEvents()
        self.step += 1 #步數+1
        self.labelStep.setText("已用步數： " + str(self.step))
        self.buttonNextStep.setEnabled(self.step != self.totalStep)

    def AI_AutoComplete(self, delayTime):
        self.AI_NextStep()
        if self.step != self.totalStep:
            threading.Timer(delayTime, lambda: self.AI_AutoComplete(delayTime)).start()
            # print("Fuck Qt")

    # Add
    def CreateRandomPuzzle(self):
        buttonCount = self.data.GetButtonCount()
        # region 接龍哥API
        # matrix = [[2, 3, 12, 8],
        #           [6, 13, 4, 5],
        #           [0, 10, 7, 1],
        #           [11, 14, 15, 9]]
        # self.puzzle = matrix
        print("Random Puzzle : ", self.puzzle)
        buttonNullIndex = self.data.GetNowNullButtonIndex()

        print("nullIndex: " + str(buttonNullIndex))
        print("modori: ")
        self.puzzle = self.data.GetPuzzle()
        print(self.puzzle)
        #endregion

        #region 接生佬API 得到每步走法
        self.nullBtnIndexRow, self.nullBtnIndexCol = FuntionTools.FindNumberFormMatrix(self.puzzle, 0)
        self.puzzlePath = PA.NPuzzle(self.nullBtnIndexCol, self.nullBtnIndexRow, self.puzzle)
        self.movePath, self.totalStep = PA.test_best_first_search(self.puzzlePath)  # 得到每步走法
        #endregion

        self.AddButtonList(buttonCount)

    #目前空格所在位置, 移動走法
    def MoveButton(self, nullRow, nullCol, moveStep):
        # print(moveStep)
        if moveStep == "up":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow - 1][nullCol] = self.buttonList[nullRow - 1][nullCol], self.buttonList[nullRow][nullCol]
            return nullRow - 1, nullCol

        elif moveStep == "down":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow + 1][nullCol] = self.buttonList[nullRow + 1][nullCol], self.buttonList[nullRow][nullCol]
            return nullRow + 1, nullCol

        elif moveStep == "left":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow][nullCol - 1] = self.buttonList[nullRow][nullCol - 1], self.buttonList[nullRow][nullCol]
            return nullRow, nullCol - 1

        elif moveStep == "right":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow][nullCol + 1] = self.buttonList[nullRow][nullCol + 1], self.buttonList[nullRow][nullCol]
            return nullRow, nullCol + 1

    def UpdateButtonPosition(self):
        size = 100
        dBtnSize = (10, 10)
        count = self.data.GetButtonCount()
        for i in range(count):
            for j in range(count):
                self.buttonList[i][j].move(dBtnSize[0] + j * size, dBtnSize[1] + i * size)

    #test - 以下幾乎都重複程式碼 臭臭的喔
    def AddButtonList(self, addRowButtonCount):
        self.ClearButton()
        pixmapList = self.data.GetPixmapList()
        for i in range(addRowButtonCount):
            rowButtonList = []
            for j in range(addRowButtonCount):
                imgIndex = self.puzzle[i][j]
                buttonIndex = i * addRowButtonCount + j
                if pixmapList:  # test 用
                    rowButtonList.append(self.AddButton(j, i, imgIndex, pixmapList[imgIndex]))
                else:
                    rowButtonList.append(self.AddButton2(j, i, imgIndex))

            self.buttonList.append(rowButtonList)

    #test - no image
    def AddButton2(self, row, column, buttonIndex):
        size = 100
        dButtonPos = (10, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.setVisible(buttonIndex != 0)
        #newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))
        return newButton

    def AddButton(self, row, column, buttonIndex, pixmap):
        size = 100
        dButtonPos = (10, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.setAutoFillBackground(True)
        newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))
        newButton.setFlat(True)

        colNum = self.data.GetButtonCount()
        lastIndex = ((colNum ** 2) - 1)
        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        if buttonIndex != 0:
            newButton.setStyleSheet("border-image: url(subImage/" + str(buttonIndex - 1) + ".jpg);")
        else:
            newButton.setStyleSheet("border-image: url(subImage/" + str(lastIndex) + ".jpg);")
        newButton.setVisible(buttonIndex != 0)
        newButton.setEnabled(buttonIndex != 0)

        return newButton

    def ClearButton(self):
        for rowBtn in self.buttonList:
            for btn in rowBtn:
                btn.deleteLater()
        self.buttonList.clear()

    def ClickSaveButton(self):
        self.data.SaveData(self.puzzlePath, self.movePath, self.step, self.totalStep)
        self.data.SetPuzzle(self.puzzle)
        print("Click save data")
        FuntionTools.writeJson("data.json", self.data)