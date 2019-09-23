from PyQt5 import QtCore, QtGui, QtWidgets

class CompleteDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 155)
        self.labelCongratulations = QtWidgets.QLabel(Dialog)
        self.labelCongratulations.setGeometry(QtCore.QRect(90, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCongratulations.setFont(font)
        self.labelCongratulations.setObjectName("labelCongratulations")
        self.buttonRetry = QtWidgets.QPushButton(Dialog)
        self.buttonRetry.setGeometry(QtCore.QRect(60, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRetry.setFont(font)
        self.buttonRetry.setObjectName("buttonRetry")
        self.buttonMenu = QtWidgets.QPushButton(Dialog)
        self.buttonMenu.setGeometry(QtCore.QRect(210, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMenu.setFont(font)
        self.buttonMenu.setObjectName("buttonMenu")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelCongratulations.setText(_translate("Dialog", "Puzzle Solve !"))
        self.buttonRetry.setText(_translate("Dialog", "再來一局"))
        self.buttonMenu.setText(_translate("Dialog", "回主畫面"))

