from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import sys

class CompleteDialog(QDialog):
    def __init__(self):
        super(CompleteDialog, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(388, 155)
        self.labelCongratulations = QtWidgets.QLabel(self)
        self.labelCongratulations.setGeometry(QtCore.QRect(90, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.labelCongratulations.setFont(font)
        self.labelCongratulations.setObjectName("labelCongratulations")
        self.buttonRetry = QtWidgets.QPushButton(self)
        self.buttonRetry.setGeometry(QtCore.QRect(60, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRetry.setFont(font)
        self.buttonRetry.setObjectName("buttonRetry")
        self.buttonMenu = QtWidgets.QPushButton(self)
        self.buttonMenu.setGeometry(QtCore.QRect(210, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonMenu.setFont(font)
        self.buttonMenu.setObjectName("buttonMenu")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelCongratulations.setText(_translate("Dialog", "Puzzle Solve !"))
        self.buttonRetry.setText(_translate("Dialog", "再來一局"))
        self.buttonMenu.setText(_translate("Dialog", "回主畫面"))
