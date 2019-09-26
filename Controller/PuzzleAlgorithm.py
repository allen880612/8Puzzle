#!/usr/bin/env python
# coding: utf-8

# # 使用人工智慧演算法來解決數字推盤遊戲

# ## 產生拼圖類別以及實現基本操作

# In[1]:


import copy
from Controller import FuntionTools

class NPuzzle:
    """數字推盤類別，推盤大小根據輸入的矩陣決定。
    
    Usage:
        NPuzzle(x, y, matrix)，其中
            x, y: 空格位置。
            matrix: 拼圖本體為長=寬=size的矩陣，儲存數字0~(size-1)，
                其中0表示空格。
    """
    
    def __init__(self, x=None, y=None, matrix=None):
        # 輸入為空則設定為已完成的的3*3拼圖
        if x is y is matrix is None:
            x, y, matrix = self._creat_goal_matrix(3)
            
        self.size = len(matrix)
        self.x = x
        self.y = y
        self.matrix = matrix
        
    @staticmethod
    def _creat_goal_matrix(size):
        """產生推盤目標狀態，回傳空格位置以及矩陣。"""
        x = y = size - 1
        matrix = [[x + y * size for x in range(size)] for y in range(size)]
        
        return 0, 0, matrix
    
    @property
    def goal(self):
        """回傳目標推盤。"""
        return self.__class__(
            *self._creat_goal_matrix(self.size))
    
    def __eq__(self, other):
        return self.matrix == other.matrix
    
    def __gt__(self, other):
        # 臭的寫法，為了使heap比較不報錯才新增這個函式
        if isinstance(other, self.__class__):
            return self.size > other.size
        else:
            return NotImplemented
    
    def is_done(self):
        """檢查推盤是否為目標狀態。"""
        return ((self.x, self.y, self.matrix)
            == self._creat_goal_matrix(self.size))
        
    def __repr__(self):
        return f'NPuzzle({self.matrix})'
    
    def __str__(self):
        
        def get_lines():
            for row in self.matrix:
                yield ' '.join(map(str, row))
                
        puzzle = '\n'.join(get_lines())
        split = '-' * (self.size * 2 - 1)
        
        return f'{split}\n{puzzle}\n{split}'
            
    def move(self, direction):
        """產生移動後的推盤，如果無法移動則回傳None。
        其中參數direction對應所對應的方向分別為：
            'up': 上, 'down': 下, 'left': 左, 'right': 右
        """
        # 根據方向判斷要與空格交換的座標
        COORDS_OF_DIR = {
            'up': (self.x, self.y - 1),
            'down': (self.x, self.y + 1),
            'left': (self.x - 1, self.y),
            'right': (self.x + 1, self.y),
        }
        
        x, y = COORDS_OF_DIR.get(direction)
        # 不超出邊界
        if 0 <= x < self.size and 0 <= y < self.size:
            new_matrix = copy.deepcopy(self.matrix)
            new_matrix[self.y][self.x], new_matrix[y][x] = (
                new_matrix[y][x], new_matrix[self.y][self.x])
            return self.__class__(x, y, new_matrix)
        else:
            return None
        
    @property
    def nextstates(self):
        """產生當前狀態所有可能的下一個狀態"""
        DIRS = ('up', 'down', 'left', 'right')
        
        states = list()
        for dir_ in DIRS:
            state = self.move(dir_)
            if state:
                states.append(state)
            
        return states
    
    def __hash__(self):
        
        def get_lines():
            for row in self.matrix:
                yield ''.join(map(str, row))
                
        return hash(''.join(get_lines()))
                    


# 測試類別是否可以正常使用

# In[2]:

testMatrix = [[7, 4, 8], [2, 1, 3], [0, 6, 5]]
puzzle = NPuzzle(0, 2, testMatrix)
print(puzzle)
print(f'is done? {puzzle.is_done()}')
print()

# puzzle = puzzle.move('up')
# puzzle = puzzle.move('up')
# puzzle = puzzle.move('down')
# puzzle = puzzle.move('left')
# puzzle = puzzle.move('left')
# puzzle = puzzle.move('right')
# print(puzzle)
# print(f'is done? {puzzle.is_done()}')
# print()

# for state in puzzle.nextstates:
#     print(state)


# ## 最佳優先搜尋

# 設計評估函式

# In[58]:


def calc_diffrence(puzzle):
    """計算與目標狀態的差異值"""
    goal = puzzle.goal
    
    sum_ = 0
    for y in range(puzzle.size):
        for x in range(puzzle.size):
            if puzzle.matrix[y][x] != goal.matrix[y][x]:
                sum_ += 1
            '''if puzzle.matrix[y][x] != 0:
                truey, truex = divmod(puzzle.matrix[y][x] - 1, puzzle.size)
                sum_ += abs(x - truex) + abs(y - truey)'''
    
    return sum_


# 實作演算法

# In[77]:


import heapq


def best_first_search(start, max_times):
    """利用最佳優先搜尋來尋找目標狀態。回傳目標狀態以及路徑"""
    
    def creat_item(puzzle):
        """產生裝在堆疊中用的item，以長度為2的tuple儲存，
        前者為評估函數，後者為推盤狀態。
        """
        return calc_diffrence(puzzle), puzzle
    
    # 儲存展開後狀態的上個狀態，用來回溯完成路徑
    previous_states = dict()
    # 儲存已經拜訪過的狀態
    visiteds = set()

    # 產生算法中所使用的堆疊，並把開始狀態裝入堆疊
    heap = list()
    heapq.heappush(heap, creat_item(start))
    times = 0
    while heap and not heap[0][1].is_done() and times < max_times:
            # 如果堆疊還有元素可以展開，且最優先之狀態不等於目標狀態\
        # 從堆疊中拿出最優先的狀態，並展開
        diff, top_priority = heapq.heappop(heap)
        for state in top_priority.nextstates:
            if state not in visiteds:
                    # 如果該狀態沒有被搜尋過，加入到堆疊中，並記錄其上一個狀態
                heapq.heappush(heap, creat_item(state))
                previous_states.setdefault(state, top_priority)
        
        visiteds.add(top_priority)
        times += 1
    
    final = heap[0][1] if heap else None
    
    # 回溯路徑
    path = list()
    movePath = list()
    
    current = final
    while current != start:
        path.append(current)
        current = previous_states[current]
    path.append(start)
    path.reverse()

    startRow, startColumn = FuntionTools.FindNumberFormMatrix(path[0].matrix, 0)
    print("rref")
    print(startRow, startColumn)

    # print("print step")
    # for step in path:
    #     print(step)

    #算走法
    for step in range(1, len(path)):
        startRow, startColumn, moveStep = GetMove(startRow, startColumn, path[step].matrix)
        movePath.append(moveStep)

    for state in movePath:
        print(state)

    return final, path, movePath


# 用來測試算法的函式

# In[81]:

#計算走法
def GetMove(row, col, compareMatrix):
    zeroRow, zeroCol = FuntionTools.FindNumberFormMatrix(compareMatrix, 0)
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


def test_best_first_search(start, max_times=10000):
    """輸入開始狀態產生結果"""
    print('start')
    print(start)
    print()

    print('goal')
    print(start.goal)
    print()
    
    final, path, movePath = best_first_search(start, max_times)
    
    if path[-1] == start.goal:
        print(f'step: {len(path) - 1}')
        print('path')
        for state in path:
            print(state)
        # for state in path:
        #     print(movePath)
    else:
        print('找不到目標狀態!')
    return movePath, len(path) - 1

# In[55]:
#test_best_first_search(puzzle)
'''
start = NPuzzle(1, 1, [
    [4, 1, 2],
    [5, 0, 3],
    [7, 8, 6]
])
test_best_first_search(start)


# In[56]:


start = NPuzzle(2, 2, [
    [1, 2, 3],
    [4, 5, 6],
    [8, 7, 0]
])
test_best_first_search(start)


# In[62]:


start = NPuzzle(1, 1, [
    [8, 6, 4],
    [3, 0, 1],
    [2, 7, 5]
])
test_best_first_search(start)


# In[74]:


start = NPuzzle(0, 2, [
    [1, 8, 5],
    [2, 4, 7],
    [0, 3, 6]
])
test_best_first_search(start, 10000)


# In[75]:


start = NPuzzle(1, 1, [
    [8, 6, 2],
    [7, 0, 1],
    [5, 4, 3]
])
test_best_first_search(start)


# In[76]:


start = NPuzzle(1, 1, [
    [1, 3, 5],
    [8, 0, 2],
    [7, 6, 4]
])
test_best_first_search(start)


# In[78]:


start = NPuzzle(1, 1, [
    [5, 6, 8],
    [1, 0, 4],
    [7, 3, 2]
])
test_best_first_search(start)


# In[80]:


start = NPuzzle(0, 2, [
    [2, 3, 12, 8],
    [6, 13, 4, 5],
    [0, 10, 7, 1],
    [11, 14, 15, 9]
])
test_best_first_search(start, 10000)
'''

# In[ ]:




