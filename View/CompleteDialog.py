from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from View import UI
import sys

class CompleteDialog(QDialog):
    def __init__(self):
        super(CompleteDialog, self).__init__()
        self.ui = UI.Ui_CompleteDialog()
        self.ui.setupUi(self)

        self.ui.buttonMenu.clicked.connect(self.close)
        self.ui.buttonRetry.clicked.connect(self.close)

