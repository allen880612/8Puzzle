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
        self.buttonMatrix = None

        self.sourceImage = None
        self.sourceQPixmap = None
        self.pixmapList = False

        self.puzzle = None  # 依照再initWindow按下的按鈕，建立之puzzle

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

    def SetPuzzle(self, puzzle):
        self.puzzle = puzzle

    def GetPuzzle(self):
        return self.puzzle

    def SetButtonMatrix(self, matrix):
        self.buttonMatrix

    def GetButtonMatrix(self):
        return self.buttonMatrix