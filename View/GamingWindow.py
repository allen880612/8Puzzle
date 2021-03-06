from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from Controller import RandomPuzzle
from Controller import FuntionTools
from Controller import PuzzleAlgorithm as PA
from Controller import AStar as AS
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
        self.aStar = None  # 綱老函式

        self.puzzlePath = None
        self.storeStep = 0
        self.step = 0  # now step
        self.totalStep = 0  # 演算法總共要走的步數
        self.movePath = None  # 每步的移動
        self.nullBtnIndexRow, self.nullBtnIndexCol = 0, 0  #目前的空按鈕位置

        self.IsAutoFinishing = False
        self.delayTime = 0.05
        self.auto_thread = Timer(self.delayTime, self.AI_AutoComplete)

        self.IsUserPlayed = False


    def ClearWindowsData(self):
        self.puzzle.clear()
        self.ClearButton()
        self.bestSearch = None
        self.aStar = None
        self.puzzlePath = None
        self.storeStep = self.data.GetStep()
        self.step = 0  # now step
        self.totalStep = 0  # 演算法總共要走的步數
        self.movePath = None  # 每步的移動
        self.nullBtnIndexRow, self.nullBtnIndexCol = 0, 0  # 目前的空按鈕位置

        self.ui.buttonAutoFinish.setEnabled(True)
        self.SetButtonEnable(True)
        self.ui.buttonAutoFinish.setText("AI自動完成")
        self.IsAutoFinishing = False
        self.ui.labelStep.setText("已用步數： " + str(self.storeStep))

        self.completeDialog = CD.CompleteDialog()
        self.DialogSetting()

        self.IsUserPlayed = False

    def UISetting(self):
        self.ui.buttonNextStep.clicked.connect(self.AI_NextStep)
        self.ui.buttonAutoFinish.clicked.connect(self.ClickAIAutoFinish)
        self.ui.buttonSave.clicked.connect(self.ClickSaveButton)
        self.ui.buttonMenu.clicked.connect(self.ReturnMenu)
        self.ui.buttonRestart.clicked.connect(self.ReStart)
        self.ui.buttonNextStep_2.clicked.connect(self.AStar_NextStep)
        self.DialogSetting()

    def DialogSetting(self):
        self.completeDialog.ui.buttonRetry.clicked.connect(self.ReStart)

    def ReturnMenu(self):
        self.data.Clear()

    def ReStart(self):
        print("restart")
        self.ClearWindowsData()
        buttonCount, nullButtonIndex = self.data.GetButtonCount(), self.data.GetNowNullButtonIndex()
        #imagePath = self.data.GetImagePath()
        #self.data.Clear()
        puzzleControl = RP.RandomMatrix(buttonCount)
        puzzleControl.ResetPuzzleBlankLocation(nullButtonIndex)
        #self.data.SetButtonCount(buttonCount)
        #self.data.SetNowNullButtonIndex(nullButtonIndex)
        self.data.SetPuzzle(puzzleControl.GetPuzzle())
        #self.data.SetImagePath(imagePath)
        self.CreateRandomPuzzle()

    # Add
    def ReviceMessage(self, message):
        if message == "Goto3":
            print("Revice! " + message)
            self.ClearWindowsData()
            self.CreateRandomPuzzle()

    def Move(self, moveStep):
        # print(self.nullBtnIndexRow, self.nullBtnIndexCol)
        self.nullBtnIndexRow, self.nullBtnIndexCol = self.MoveButton(self.nullBtnIndexRow, self.nullBtnIndexCol, moveStep)
        self.UpdateButtonPosition()
        #QtWidgets.QApplication.processEvents()
        self.step += 1 #步數+1
        self.ui.labelStep.setText("已用步數： " + str(self.storeStep + self.step))
        # 完成Puzzle事件
        if self.IsFinished():
            self.SetButtonEnable(True)
            self.ui.buttonNextStep.setEnabled(False)
            self.ui.buttonAutoFinish.setEnabled(False)
            self.ui.buttonNextStep_2.setEnabled(False)
            print("Puzzle finished!")
            self.CompletePazzle()
            print("Complete Dialog closed")

    #Add connect
    def AI_NextStep(self):
        if self.IsUserPlayed: #使用者曾經玩過
            self.AI_ComputePath() #先重新算一次

        self.Move(self.movePath[self.step])

    def ClickAIAutoFinish(self):
        self.IsAutoFinishing = not self.IsAutoFinishing
        self.SetButtonEnable(not self.IsAutoFinishing)
        if self.IsAutoFinishing:
            self.ui.buttonAutoFinish.setText("暫停AI自動完成")
        else:
            self.ui.buttonAutoFinish.setText("AI自動完成")

        self.AI_AutoComplete()
        # self.AI_AutoComplete(0.05)

    def AI_AutoComplete(self):
        # 停止 thread
        if self.IsFinished():
            self.auto_thread.cancel()
        elif self.IsAutoFinishing:
            self.AI_NextStep()
            self.auto_thread = Timer(self.delayTime, self.AI_AutoComplete)
            self.auto_thread.start()

    # 生佬演算法
    def AI_ComputePath(self):
        self.nullBtnIndexRow, self.nullBtnIndexCol = FuntionTools.FindNumberFormMatrix(self.puzzle, 0)
        self.puzzlePath = PA.NPuzzle(self.nullBtnIndexCol, self.nullBtnIndexRow, self.puzzle)
        self.bestSearch = PA.test_best_first_search(self.puzzlePath)
        self.movePath = self.bestSearch.GetMovePath()
        self.totalStep = self.bestSearch.GetTotalStep()
        self.storeStep += self.step
        self.step = 0
        self.IsUserPlayed = False

    def AStar_NextStep(self):
        if self.IsUserPlayed: #使用者曾經玩過
            self.AStar_ComputePath() #先重新算一次

        self.Move(self.movePath[self.step])

    # 綱老A*
    def AStar_ComputePath(self):
        self.aStar = AS.Puzzle(self.puzzle)
        self.nullBtnIndexRow, self.nullBtnIndexCol = FuntionTools.FindNumberFormMatrix(self.puzzle, 0)
        self.puzzlePath = self.aStar.GetPath()
        self.totalStep = self.aStar.GetTotalStep()
        self.movePath = self.aStar.GetMovePath()
        self.storeStep += self.step
        self.step = 0
        self.IsUserPlayed = False

    # Add
    def CreateRandomPuzzle(self):
        buttonCount = self.data.GetButtonCount()
        print("button count: " + str(buttonCount))

        # region 接龍哥API
        buttonNullIndex = self.data.GetNowNullButtonIndex()
        self.puzzle = self.data.GetPuzzle()
        print("Random Puzzle : ")
        print(self.puzzle)
        #endregion

        #region 接生佬API 得到每步走法
        self.AI_ComputePath()
        if buttonCount <= 3:
            self.AStar_ComputePath()
        else:
            self.ui.buttonNextStep_2.setEnabled(False)
        #endregion

        self.AddButtonList(buttonCount)

    #目前空格所在位置, 移動走法
    def MoveButton(self, nullRow, nullCol, moveStep):
        # print(moveStep)
        if moveStep == "up":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow - 1][nullCol] = self.buttonList[nullRow - 1][nullCol], self.buttonList[nullRow][nullCol]
            self.puzzle[nullRow][nullCol], self.puzzle[nullRow - 1][nullCol] = self.puzzle[nullRow - 1][nullCol], self.puzzle[nullRow][nullCol]
            return nullRow - 1, nullCol

        elif moveStep == "down":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow + 1][nullCol] = self.buttonList[nullRow + 1][nullCol], self.buttonList[nullRow][nullCol]
            self.puzzle[nullRow][nullCol], self.puzzle[nullRow + 1][nullCol] = self.puzzle[nullRow + 1][nullCol], self.puzzle[nullRow][nullCol]
            return nullRow + 1, nullCol

        elif moveStep == "left":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow][nullCol - 1] = self.buttonList[nullRow][nullCol - 1], self.buttonList[nullRow][nullCol]
            self.puzzle[nullRow][nullCol], self.puzzle[nullRow][nullCol - 1] = self.puzzle[nullRow][nullCol - 1], self.puzzle[nullRow][nullCol]
            return nullRow, nullCol - 1

        elif moveStep == "right":
            self.buttonList[nullRow][nullCol], self.buttonList[nullRow][nullCol + 1] = self.buttonList[nullRow][nullCol + 1], self.buttonList[nullRow][nullCol]
            self.puzzle[nullRow][nullCol], self.puzzle[nullRow][nullCol + 1] = self.puzzle[nullRow][nullCol + 1], self.puzzle[nullRow][nullCol]
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

    def ClickImageButtion(self, button):
        # buttonPuzzle = []
        # for i in self.buttonList:
        #     btnl = []
        #     for j in i:
        #         btnl.append(j.name())
        #     buttonPuzzle.append(btnl)
        size = 100
        posx, posy = button.pos().x(), button.pos().y()
        btnRow, btnCol = posy // size, posx // size
        print("{%d, %d}" % (btnRow, btnCol))
        if FuntionTools.IsAround((self.nullBtnIndexRow, self.nullBtnIndexCol), (btnRow, btnCol)):
            #self.Move()
            movedir = FuntionTools.GetPlayerMove((self.nullBtnIndexRow, self.nullBtnIndexCol), (btnRow, btnCol))
            self.Move(movedir)
            self.IsUserPlayed = True

    def SetButtonEnable(self, flag):
        self.ui.buttonMenu.setEnabled(flag)
        self.ui.buttonNextStep.setEnabled(flag)
        self.ui.buttonNextStep_2.setEnabled(flag and self.data.GetButtonCount() <= 3)
        self.ui.buttonRestart.setEnabled(flag)
        self.ui.buttonSave.setEnabled(flag)

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
        newButton.clicked.connect(lambda :self.ClickImageButtion(newButton))
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
        newButton.clicked.connect(lambda: self.ClickImageButtion(newButton))
        newButton.setFlat(True)

        colNum = self.data.GetButtonCount()
        lastIndex = ((colNum ** 2) - 1)
        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        if buttonIndex != 0:
            newButton.setStyleSheet("border-image: url(subImage/" + str(buttonIndex - 1) + ".png);")
        else:
            newButton.setStyleSheet("border-image: url(subImage/" + str(lastIndex) + ".png);")
        newButton.setVisible(buttonIndex != 0)
        newButton.setEnabled(buttonIndex != 0)

        return newButton

    def ClearButton(self):
        for rowBtn in self.buttonList:
            for btn in rowBtn:
                btn.deleteLater()
        self.buttonList.clear()

    def ClickSaveButton(self):
        self.data.SaveData(self.puzzlePath, self.movePath, self.step + self.storeStep, self.totalStep)
        self.data.SetPuzzle(self.puzzle)
        # self.data.SetPuzzle(self.bestSearch.GetNowPuzzleState(self.step))
        # self.data.SetPuzzle(self.aStar.GetStateFromStates(self.step))
        print("test")
        print(self.data.GetPuzzle())
        print(type(self.data.GetPuzzle()))
        print("Click save data")
        FuntionTools.writeJson("data.json", self.data)

    # 完成Puzzle 之Dialog
    def CompletePazzle(self):
        print("CompletePazzle Begin")
        # self.completeDialog = CD.CompleteDialog()
        # self.DialogSetting()
        self.completeDialog.exec_()
        print("CompletePazzle End")

    def IsFinished(self):
        try:
            return self.puzzle == self.bestSearch.GetGoal()
        except:
            return False