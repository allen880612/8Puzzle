from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from Controller import RandomPuzzle
from Controller import FuntionTools
from Controller import PuzzleAlgorithm as PA
from Controller import RandomPuzzle as RP
from View import CompleteDialog as CD
from View import UI
from threading import Timer
import json

class GameWindow(QMainWindow):
    def __init__(self, data):
        super(GameWindow, self).__init__()
        self.ui = UI.Ui_GameWindow()
        self.ui.setupUi(self)
        self.completeDialog = CD.CompleteDialog()
        self.UISetting()

        self.data = data
        self.data.dataSignal.signal.connect(self.ReviceMessage)
        self.puzzle = []  #add
        self.buttonList = []  #add

        self.bestSearch = None  # 生佬的函式

        self.puzzlePath = None
        self.step = 0  # now step
        self.totalStep = 0  # 演算法總共要走的步數
        self.movePath = None  # 每步的移動
        self.nullBtnIndexRow, self.nullBtnIndexCol = 0, 0  #目前的空按鈕位置

        self.IsAutoFinishing = False
        self.auto_thread = Timer(0.05, self.AI_AutoComplete)



    def ClearWindowsData(self):
        self.puzzle.clear()
        self.ClearButton()
        self.bestSearch = None
        self.puzzlePath = None
        self.step = 0  # now step
        self.totalStep = 0  # 演算法總共要走的步數
        self.movePath = None  # 每步的移動
        self.nullBtnIndexRow, self.nullBtnIndexCol = 0, 0  # 目前的空按鈕位置

        self.ui.buttonNextStep.setEnabled(True)
        self.ui.buttonAutoFinish.setEnabled(True)
        self.ui.buttonAutoFinish.setText("AI自動完成")
        self.IsAutoFinishing = False
        self.ui.labelStep.setText("已用步數： 0")

    def UISetting(self):
        self.ui.buttonNextStep.clicked.connect(self.AI_NextStep)
        self.ui.buttonAutoFinish.clicked.connect(self.ClickAIAutoFinish)
        self.ui.buttonSave.clicked.connect(self.ClickSaveButton)
        self.ui.buttonMenu.clicked.connect(self.ReturnMenu)
        self.ui.buttonRestart.clicked.connect(self.ReStart)
        self.completeDialog.ui.buttonMenu.clicked.connect(self.ReturnMenu)
        self.completeDialog.ui.buttonRetry.clicked.connect(self.ReStart)

    def ReturnMenu(self):
        self.data.Clear()

    def ReStart(self):
        print("restart")
        self.ClearWindowsData()
        buttonCount, nullButtonIndex = self.data.GetButtonCount(), self.data.GetNowNullButtonIndex()
        self.data.Clear()
        puzzleControl = RP.RandomMatrix(self.data, buttonCount)
        puzzleControl.ResetPuzzleBlankLocation(nullButtonIndex)
        self.data.SetButtonCount(buttonCount)
        self.data.SetNowNullButtonIndex(nullButtonIndex)
        self.data.SetPuzzle(puzzleControl.GetPuzzle())
        self.CreateRandomPuzzle()

    # Add
    def ReviceMessage(self, message):
        if message == "Goto3":
            print("Revice! " + message)
            self.ClearWindowsData()
            self.CreateRandomPuzzle()

    #Add connect
    def AI_NextStep(self):
        #print(self.nullBtnIndexRow, self.nullBtnIndexCol)
        self.nullBtnIndexRow, self.nullBtnIndexCol = self.MoveButton(self.nullBtnIndexRow, self.nullBtnIndexCol, self.movePath[self.step])
        self.UpdateButtonPosition()
        #QtWidgets.QApplication.processEvents()
        self.step += 1 #步數+1
        self.ui.labelStep.setText("已用步數： " + str(self.step))
        # 完成Puzzle事件
        if self.IsFinished():
            self.ui.buttonNextStep.setEnabled(False)
            self.ui.buttonAutoFinish.setEnabled(False)
            print("Puzzle finished!")
            self.CompletePazzle()
            print("Really?")

    def ClickAIAutoFinish(self):
        self.IsAutoFinishing = not self.IsAutoFinishing
        if self.IsAutoFinishing:
            self.ui.buttonAutoFinish.setText("暫停AI自動完成")
        else:
            self.ui.buttonAutoFinish.setText("AI自動完成")

        self.AI_AutoComplete()
        # self.AI_AutoComplete(0.05)

    def AI_AutoComplete(self):
        # print("Enter Auto")
        # 停止 thread
        if self.IsFinished():
            print("stop it please")
            self.auto_thread.cancel()
            print("...")
        elif self.IsAutoFinishing:
            self.AI_NextStep()
            self.auto_thread = Timer(0.05, self.AI_AutoComplete)
            self.auto_thread.start()

    # def AI_AutoComplete(self, delayTime):
    #     auto_thread = Timer(delayTime, lambda: self.AI_AutoComplete(delayTime))
    #     if self.IsFinished():
    #         auto_thread.cancel()
    #         print("cancel thread")
    #     if self.IsAutoFinishing:
    #         auto_thread.start()
    #         self.AI_NextStep()

    # Add
    def CreateRandomPuzzle(self):
        buttonCount = self.data.GetButtonCount()
        print(buttonCount)
        # region 接龍哥API
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
        self.bestSearch = PA.test_best_first_search(self.puzzlePath)
        self.movePath = self.bestSearch.GetMovePath()
        self.totalStep = self.bestSearch.GetTotalStep()
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

    def ClickImageButtion(self, buttonIndex):
        buttonPuzzle = []
        for i in self.buttonList:
            btnl = []
            for j in i:
                btnl.append(j.objectName())
            buttonPuzzle.append(btnl)
        btnRow, btnCol = FuntionTools.FindNumberFormMatrix()
        print("{%d, %d}" %(self.nullBtnIndexRow, self.nullBtnIndexCol))

    #test - no image
    def AddButton2(self, row, column, buttonIndex):
        size = 100
        dButtonPos = (10, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.ui.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setObjectName(str(buttonIndex))
        newButton.setFont(font)
        newButton.setVisible(buttonIndex != 0)
        newButton.clicked.connect(lambda: self.ClickImageButtion(buttonIndex))
        return newButton

    def AddButton(self, row, column, buttonIndex, pixmap):
        size = 100
        dButtonPos = (10, 10)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton(self.ui.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        # newButton.setText(str(buttonIndex))
        newButton.setObjectName(str(buttonIndex))
        newButton.setFont(font)
        newButton.setAutoFillBackground(True)
        newButton.clicked.connect(lambda: self.ClickImageButtion(buttonIndex))
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
        self.data.SetPuzzle(self.bestSearch.GetNowPuzzleState(self.step))
        print("test")
        print(self.data.GetPuzzle())
        print(type(self.data.GetPuzzle()))
        print("Click save data")
        FuntionTools.writeJson("data.json", self.data)

    # 完成Puzzle 之Dialog
    def CompletePazzle(self):
        print("CompletePazzle Begin")
        # dialog_ui = CD.Ui_Dialog()
        # dialog_ui.setupUi(self.completeDialog)
        # self.completeDialog.exec_()
        self.completeDialog.exec()
        print("CompletePazzle End")


    def IsFinished(self):
        return self.step == self.totalStep