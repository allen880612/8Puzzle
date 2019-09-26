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