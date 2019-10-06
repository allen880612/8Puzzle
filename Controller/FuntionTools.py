import json
from Model import DataModel as DM

# 在二維陣列中尋找 指定number (找不到回傳-1,-1)
def FindNumberFormMatrix(matrix, number):
    row, column = -1, -1
    tempr = 0
    for rows in matrix:
        try:
            column = rows.index(number)
            row = tempr
        except:
            pass
        tempr += 1
    return row, column

def Swap(a, b):
    return b, a

def IsAround(nullPos, comparePos):
    return ((nullPos[0] == comparePos[0] and nullPos[1] == comparePos[1] - 1) or
            (nullPos[0] == comparePos[0] and nullPos[1] == comparePos[1] + 1) or
            (nullPos[0] == comparePos[0] - 1 and nullPos[1] == comparePos[1]) or
            (nullPos[0] == comparePos[0] + 1 and nullPos[1] == comparePos[1]))

#計算走的路徑
def GetPlayerMove(nullPos, comparePos):
    # 1, 1 null
    # 0, 1 this up
    move = "up"
    if nullPos[0] == comparePos[0] + 1:
        move = "up"
    elif nullPos[0] == comparePos[0] - 1:
        move = "down"
    elif nullPos[1] == comparePos[1] + 1:
        move = "left"
    elif nullPos[1] == comparePos[1] - 1:
        move = "right"
    return move

#計算走法
def GetMove(row, col, compareMatrix):
    zeroRow, zeroCol = FindNumberFormMatrix(compareMatrix, 0)
    move = "up"
    if zeroRow == row - 1:
        move = "up"
    elif zeroRow == row + 1:
        move = "down"
    elif zeroCol == col - 1:
        move = "left"
    elif zeroCol == col + 1:
        move = "right"
    return zeroRow, zeroCol, move

class UserJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__jsonencode__'):
            return obj.__jsonencode__()
        return json.JSONEncoder.default(self, obj)

#mudamuda
def __dictToDataModel(dictionary):
    if isinstance(dictionary, dict):
        data = DM.DataModel(dictionary["rowButtonCount"], dictionary["movePath"], dictionary["step"], dictionary["totalStep"])
        data.SetPuzzle(dictionary["puzzle"])
        return data

def writeJson(savePath, obj):
    print(json.dump(obj, open(savePath, "w"), cls=UserJSONEncoder))
    print("write json")

def readJson(loadPath):
    jsonData = json.load(open(loadPath))
    print("load json")
    return jsonData


def CovertIntegerToDtring(intPuzzle):
    strPuzzle = intPuzzle
    size = len(intPuzzle)
    for row in range(size):
        for col in range(size):
            strPuzzle[row][col] = str(intPuzzle[row][col])
    return strPuzzle
