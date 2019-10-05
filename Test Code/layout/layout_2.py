import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton

#
# grid addWidget example
#
# grid.setSpacing(10) #設置元件見據為10像素
# addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0) #  Alignment 對齊?
#

class ButtonGrid(QWidget):
    def __init__(self, rowCount):
        super().__init__()
        self.rowCount = rowCount
        self.buttonList = []
        self.state = None  # 亂數產生完的狀態
        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(self.rowCount)
        self.CreateButton()
        # grid.addWidget(title, 1, 0)
        # grid.addWidget(titleEdit, 1, 1)

        # grid.addWidget(author, 2, 0)
        # grid.addWidget(authorEdit, 2, 1)

        # grid.addWidget(review, 3, 0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)
        self.setLayout(self.grid)

        self.setGeometry(300, 300, 480, 480)
        self.setWindowTitle("Review")
        self.show()
    
    def CreateButton(self):
        self.AddButtonList(self.rowCount)
        for i in range(self.rowCount):
            for j in range(self.rowCount):
                self.grid.addWidget(self.buttonList[i][j], i, j)

    def AddButtonList(self, addRowButtonCount):
        #pixmapList = self.data.GetPixmapList()
        for i in range(addRowButtonCount):
            rowButtonList = []
            for j in range(addRowButtonCount):
                buttonIndex = i * addRowButtonCount + j
                print(str(buttonIndex))
                # if pixmapList: # test 用
                #     rowButtonList.append(self.AddButton(j, i, buttonIndex, pixmapList[buttonIndex]))
                # else:
                rowButtonList.append(self.AddButton(j, i, buttonIndex))

                # self.grid.addWidget(self.AddButton(j, i, buttonIndex), i, j)
            self.buttonList.append(rowButtonList)


    def AddButton(self, row, column, buttonIndex):
        size = 100
        dButtonPos = (0, 0)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        newButton = QtWidgets.QPushButton()
        # newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(dButtonPos[0] + row * size, dButtonPos[1] + column * size, size, size))
        newButton.setText(str(buttonIndex))
        newButton.setFont(font)
        newButton.clicked.connect(lambda: self.ClickButton(buttonIndex))

        newButton.setMinimumWidth(100)
        newButton.setMinimumHeight(100)

        newButton.setFlat(True)
        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        newButton.setStyleSheet("border-image: url(../subImage/" + str(buttonIndex) + ".jpg);")
        # newButton.setStyleSheet("background-image: url(../subImage/" + str(buttonIndex) + ".jpg);")

        return newButton

    def ClickButton(self, buttonIndex):
        testPuzzle = [[1, 2, 0, 3],
                      [5, 6, 7, 4],
                      [9, 10, 11, 8],
                      [13, 14, 15, 12]]

        self.grid = QGridLayout()
        self.grid.setSpacing(self.rowCount)
        self.UpdateButton(testPuzzle)

    def UpdateButton(self, nowPuzzle):
        print("now State:")
        for row in nowPuzzle:
            print(row)

        for i in range(self.rowCount):
            for j in range(self.rowCount):
                buttonIndex = nowPuzzle[i][j]
                self.grid.addWidget(self.GetButtonByIndex(buttonIndex), i, j)
                # print("btnIndex = %d"%(nowPuzzle[i][j]))

    def GetButtonByIndex(self, index):
        row = index // self.rowCount
        col = index % self.rowCount
        print(("index = %s, get(%s, %s)"%(index, row, col)))
        return self.buttonList[row][col]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ButtonGrid(4)


    sys.exit(app.exec_())
