from PyQt5 import QtWidgets, QtCore

class Signal(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def Shoot(self, message):
        self.signal.emit(message)

class DataModel():
    def __init__(self):
        self.rowButtonCount = 0 # 每一列的button個數
        self.nowNullButtonIndex = 0 # 空格按鈕的索引
        self.dataSignal = Signal() # 毫無反應 只是個信號

    def SetButtonCount(self, count):
        self.rowButtonCount = count

    def GetButtonCount(self):
        return self.rowButtonCount

    def SetNowNullButtonIndex(self, btnIndex):
        self.nowNullButtonIndex = btnIndex

    def GetNowNullButtonIndex(self):
        return self.nowNullButtonIndex