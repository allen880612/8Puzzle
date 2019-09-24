from PyQt5 import QtCore, QtGui, QtWidgets
from Model import DataModel as DM

class PreGamingWindow(object):
    def __init__(self, data):
        self.data = data
        #self.signal = DM.Signal()
        self.data.signal.signal.connect(self.ReviceMessage)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setGeometry(QtCore.QRect(10, 10, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBack.setFont(font)
        self.buttonBack.setObjectName("buttonBack")
        self.labelHint = QtWidgets.QLabel(self.centralwidget)
        self.labelHint.setGeometry(QtCore.QRect(180, 400, 321, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelHint.setFont(font)
        self.labelHint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelHint.setWordWrap(False)
        self.labelHint.setObjectName("labelHint")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 10, 471, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonDynamic = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonDynamic.setObjectName("buttonDynamic")
        self.gridLayout.addWidget(self.buttonDynamic, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonBack.setText(_translate("MainWindow", "Back"))
        self.labelHint.setText(_translate("MainWindow", "點擊任意一格來開始遊戲!"))
        self.labelHint.adjustSize(); #QLabel 自適應大小
        self.buttonDynamic.setText(_translate("MainWindow", "PushButton"))

    def AddButtonList(self, addRowButtonCount):
        totalButtonCount = addRowButtonCount ** 2
        self.buttonList = []
        for i in range(addRowButtonCount):
            rowButtonList = []
            for j in range(addRowButtonCount):
                rowButtonList.append(self.AddButton(j, i))
            self.buttonList.append(rowButtonList)

        for i in range(addRowButtonCount):
            for j in range(addRowButtonCount):
                self.buttonList[i][j].setText(str(i * addRowButtonCount + j))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.buttonList[i][j].setFont(font)

    def AddButton(self, row, column):
        size = 100
        newButton = QtWidgets.QPushButton(self.centralwidget)
        newButton.setGeometry(QtCore.QRect(row * size, column * size, size, size))
        return newButton

    def ReviceMessage(self, message):
        print("Revice!")
        print(message)
        self.AddIconList(self.data.GetButtonCount())  # PIL -> QImage -> Pixmal
        self.AddButtonList(self.data.GetButtonCount())
