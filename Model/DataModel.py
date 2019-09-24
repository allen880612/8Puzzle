from PyQt5 import QtWidgets, QtCore

class Signal(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def Shoot(self, message):
        self.signal.emit(message)

    def Connect(self):
        self.signal.connect(self.Revice)

    def Revice(self, message):
        print(message)

class DataModel():
    def __init__(self):
        self.rowButtonCount = 0
        self.signal = Signal()

    def SetButtonCount(self, count):
        self.rowButtonCount = count

    def GetButtonCount(self):
        return self.rowButtonCount