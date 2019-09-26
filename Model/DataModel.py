from PyQt5 import QtWidgets, QtCore
from PIL import Image
from Controller import FuntionTools



class Signal(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def Shoot(self, message):
        self.signal.emit(message)

class DataModel():
    def __init__(self, _rowButtonCount = 0, _movePath = None, _step = 0, _totalStep = 0):
        self.rowButtonCount = _rowButtonCount # 每一列的button個數
        self.nowNullButtonIndex = 0 # 空格按鈕的索引
        self.dataSignal = Signal() # 毫無反應 只是個信號

        self.sourceImage = None
        self.sourceQPixmap = None
        self.pixmapList = False

        self.puzzle = None  # 依照再initWindow按下的按鈕，建立之puzzle

        #save
        self.puzzlePath = None # 儲存 - 生佬的路徑 (type of NPuzzle)
        self.movePath = _movePath # 儲存 - 生佬的路徑 的 走法
        self.step = _step # 儲存 - 現在的步數
        self.totalStep = _totalStep # 儲存 - 總共會走得總步數

    #json編碼  (概念: 編碼: 轉換函式換成字典 > 儲存成Json)
    #          (      解碼: 讀取Json > json.load換成字典 > 字典丟給dataModel.SetData 設置Data)
    def __jsonencode__(self):
        dataDict = {
            "rowButtonCount": self.rowButtonCount,
            #"puzzlePath": self.puzzlePath,
            "puzzle": self.puzzle,
            "movePath": self.movePath,
            "step": self.step,
            "totalStep": self.totalStep
        }
        return dataDict

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

    def SaveData(self, _puzzlePath, _movePath, _step, _totalStep):
        print("fuck")
        #region 上面四個參數
        self.puzzlePath = _puzzlePath
        self.movePath = _movePath
        self.step = _step
        self.totalStep = _totalStep
        #endregion
        print(type(self.puzzlePath))
        print(type(self.movePath))
        print(self.step)
        print(self.totalStep)

    def SetData(self, dictionary):
        if isinstance(dictionary, dict):
            self.SaveData(dictionary["rowButtonCount"], dictionary["movePath"], dictionary["step"], dictionary["totalStep"])