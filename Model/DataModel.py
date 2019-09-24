from PyQt5 import QtWidgets, QtCore
from PIL import Image



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

        self.sourceImage = None
        self.sourceQPixmap = None
        self.pixmapList = []

    def SetButtonCount(self, count):
        self.rowButtonCount = count

    def GetButtonCount(self):
        return self.rowButtonCount

    def SetSourceImage(self, image):
        self.sourceImage = image

    def GetSourceImage(self):
        return self.sourceImage

    def SetPixmap(self, image):
        self.sourceQPixmap = image

    def GetPixmap(self):
        return self.sourceQPixmap

    def SetNowNullButtonIndex(self, btnIndex):
        self.nowNullButtonIndex = btnIndex

    def GetNowNullButtonIndex(self):
        return self.nowNullButtonIndex

    def SetPixmapList(self, pixmapList):
        self.pixmapList = pixmapList

    def GetPixmapList(self):
        return self.pixmapList