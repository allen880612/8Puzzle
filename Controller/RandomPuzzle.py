import random

# # using this class like this
# puzzle = RandomMatrix(4, 12)
# for i in puzzle.GetPuzzle():
#     print(i)

class RandomMatrix(object):
    def __init__(self, rowNum):
        self.rowNum = rowNum
        self.nowBlankIndex = 0
        self.puzzle = self.RandomPuzzle(rowNum)  # 先存沒有指定空白位置的Matrix

    def RandomPuzzle(self, n):
        puzzle = [[] for i in range(n)]
        step = n * n * 100
        row = n - 1
        col = n - 1
        for i in range(n):
            for j in range(n):
                puzzle[i].append(i * n + j + 1)
        puzzle[row][col] = 0
        for i in range(step):
            move = random.randint(0, 4)
            if move == 0:
                if row > 0:
                    temp = puzzle[row - 1][col]
                    puzzle[row - 1][col] = puzzle[row][col]
                    puzzle[row][col] = temp
                    row -= 1
            elif move == 1:
                if row < n - 1:
                    temp = puzzle[row + 1][col]
                    puzzle[row + 1][col] = puzzle[row][col]
                    puzzle[row][col] = temp
                    row += 1
            elif move == 2:
                if col > 0:
                    temp = puzzle[row][col - 1]
                    puzzle[row][col - 1] = puzzle[row][col]
                    puzzle[row][col] = temp
                    col -= 1
            elif move == 3:
                if col < n - 1:
                    temp = puzzle[row][col + 1]
                    puzzle[row][col + 1] = puzzle[row][col]
                    puzzle[row][col] = temp
                    col += 1
        self.nowBlankIndex = row * n + col
        return puzzle

    # 在外面改空格位置
    def SetBlank(self, target):
        num = self.rowNum
        now = self.nowBlankIndex
        puzzle = self.puzzle
        nowrow = now // num
        nowcol = now % num
        targetrow = target // num
        targetcol = target % num
        # print ("now = (%s, %s)"%(nowrow, nowcol))
        # print ("target = (%s, %s)"%(targetrow, targetcol))

        while nowrow > targetrow:
            temp = puzzle[nowrow - 1][nowcol]
            puzzle[nowrow - 1][nowcol] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowrow -= 1
        while nowrow < targetrow:
            temp = puzzle[nowrow + 1][nowcol]
            puzzle[nowrow + 1][nowcol] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowrow += 1
        while nowcol > targetcol:
            temp = puzzle[nowrow][nowcol - 1]
            puzzle[nowrow][nowcol - 1] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowcol -= 1
        while nowcol < targetcol:
            temp = puzzle[nowrow][nowcol + 1]
            puzzle[nowrow][nowcol + 1] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowcol += 1
        self.puzzle = puzzle

    def Setblank(self, puzzle, num, now, target):
        nowrow = now // num
        nowcol = now % num
        targetrow = target // num
        targetcol = target % num
        # print ("now = (%s, %s)"%(nowrow, nowcol))
        # print ("target = (%s, %s)"%(targetrow, targetcol))

        while nowrow > targetrow:
            temp = puzzle[nowrow - 1][nowcol]
            puzzle[nowrow - 1][nowcol] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowrow -= 1
        while nowrow < targetrow:
            temp = puzzle[nowrow + 1][nowcol]
            puzzle[nowrow + 1][nowcol] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowrow += 1
        while nowcol > targetcol:
            temp = puzzle[nowrow][nowcol - 1]
            puzzle[nowrow][nowcol - 1] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowcol -= 1
        while nowcol < targetcol:
            temp = puzzle[nowrow][nowcol + 1]
            puzzle[nowrow][nowcol + 1] = puzzle[nowrow][nowcol]
            puzzle[nowrow][nowcol] = temp
            nowcol += 1
        return puzzle

    def GetPuzzle(self):
        return self.puzzle

puzzle = RandomMatrix(4)
puzzle.SetBlank(5)
for i in puzzle.GetPuzzle():
    print(i)

# puzzle, now = RandomPuzzle(10)
# count
# num = 4
# puzzle, now = RandomPuzzle(num)
# print("now = " + str(now))
# # random
# for i in puzzle:
#     print(i)
# print()
# #set blank image by index (puzzle, colnum, nowIndex, targetIndex)
# puzzle = setblank(puzzle, num, now, 5)
# for i in puzzle:
#     print(i)
