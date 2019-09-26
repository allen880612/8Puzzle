import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout,QApplication)

#
# grid addWidget example
#
# grid.setSpacing(10) #設置元件見據為10像素
# addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0) #  Alignment 對齊?
#

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Review")
        self.show()
    
    # def CreateButton():




    
    def CreateButton(self):
        self.AddButtonList(4)

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
        newButton.setStyleSheet('QPushButton{border: 0px solid;}')
        newButton.setStyleSheet("border-image: url(subImage/" + str(buttonIndex) + ".jpg);")
        return newButton
    
    def AddButtonList(self, addRowButtonCount):
        #pixmapList = self.data.GetPixmapList()
        for i in range(addRowButtonCount):
            rowButtonList = []
            for j in range(addRowButtonCount):
                buttonIndex = i * addRowButtonCount + j
                # if pixmapList: # test 用
                #     rowButtonList.append(self.AddButton(j, i, buttonIndex, pixmapList[buttonIndex]))
                # else:
                rowButtonList.append(self.AddButton2(j, i, buttonIndex)
                # self.grid.addWidget(self.AddButton2(j, i, buttonIndex), j, i)
                # self.grid.addWidget(new QPushButton(str(buttonIndex)), j, i)
            # self.buttonList.append(rowButtonList)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())