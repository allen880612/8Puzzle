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
