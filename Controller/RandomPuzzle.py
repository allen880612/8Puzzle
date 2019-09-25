import random
from Controller import FuntionTools
def RandomPuzzle(n):
    puzzle = [[] for i in range(n)]
    step = n * n * 1000
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
    return puzzle

# puzzle = RandomPuzzle(5)
# for i in puzzle:
#     print(i)
#
# print(FuntionTools.FindNumberFormMatrix(puzzle, 0))

