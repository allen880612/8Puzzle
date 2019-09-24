from PyQt5 import QtWidgets, QtCore
from PIL import Image



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

        self.sourceImage = None
        self.sourceQPixmap = None

    def SetButtonCount(self, count):
        self.rowButtonCount = count

    def GetButtonCount(self):
        return self.rowButtonCount

    def SetSourceImage(self, image):
        self.sourceImage = image

    def GetSourceImage(self):
        return self.sourceImage

    def SetQPixmap(self, image):
        self.sourceQPixmap = image

    def GetQPixmap(self):
        return self.sourceQPixmap
