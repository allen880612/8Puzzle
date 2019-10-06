import queue
import math
gameTypeNum = 3
destOrder = [1, 2, 3, 4, 5, 6, 7, 8, -1]
srcOrder = [7, 6, 1, 3, 2, 8, 4, 5, -1]
nodes = queue.Queue()

class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        self.child = []
        self.searched = False

#找到state的鄰居
def FindNeighbor(node):
    neighbor = []
    spaceOrder = FindSpaceInState(node.state)
    if CanUp(node.state, spaceOrder):
        neighbor.append(MoveUp(node, spaceOrder))
    if CanRight(node.state, spaceOrder):
        neighbor.append(MoveRight(node, spaceOrder))
    if CanDown(node.state, spaceOrder):
        neighbor.append(MoveDown(node, spaceOrder))
    if CanLeft(node.state, spaceOrder):
        neighbor.append(MoveLeft(node, spaceOrder))
    return neighbor
    
#找到state中的空白
def FindSpaceInState(state):
    for i in range(0, len(state)):
        if state[i] == -1:
            return i
        
#判斷可否向上
def CanUp(state, spaceOrder):
    return (spaceOrder - gameTypeNum) >= 0

#判斷可否向右
def CanRight(state, spaceOrder):
    return (spaceOrder % gameTypeNum) != (gameTypeNum - 1)

#判斷可否向下
def CanDown(state, spaceOrder):
    return (spaceOrder + gameTypeNum) <= (math.pow(gameTypeNum, 2) - 1)

#判斷可否向左
def CanLeft(state, spaceOrder):
    return (spaceOrder % gameTypeNum) != 0

#返回向上移動的state
def MoveUp(node, spaceOrder):
    upNode = Node(node, node.state.copy())
    node.child.append(upNode)
    upNode.state[spaceOrder], upNode.state[spaceOrder - gameTypeNum] = upNode.state[spaceOrder - gameTypeNum], upNode.state[spaceOrder]
    return upNode

#返回向右移動的state
def MoveRight(node, spaceOrder):
    rightNode = Node(node, node.state.copy())
    node.child.append(rightNode)
    rightNode.state[spaceOrder], rightNode.state[spaceOrder + 1] = rightNode.state[spaceOrder + 1], rightNode.state[spaceOrder]
    return rightNode

#返回向下移動的state
def MoveDown(node, spaceOrder):
    downNode = Node(node, node.state.copy())
    node.child.append(downNode)
    downNode.state[spaceOrder], downNode.state[spaceOrder + gameTypeNum] = downNode.state[spaceOrder + gameTypeNum], downNode.state[spaceOrder]
    return downNode

#返回向左移動的state
def MoveLeft(node, spaceOrder):
    leftNode = Node(node, node.state.copy())
    node.child.append(leftNode)
    leftNode.state[spaceOrder], leftNode.state[spaceOrder - 1] = leftNode.state[spaceOrder - 1], leftNode.state[spaceOrder]
    return leftNode

#輸入
while len(srcOrder) < 9:
    order = input()
    for x in order.split():
        srcOrder.append(int(x))

#BFS
currentNode = Node(None, srcOrder)
count = 0
stack = []
stack.append(currentNode)
isInStack = False
while currentNode.state != destOrder:
    if(len(currentNode.child) == 0 and not currentNode.searched):
        currentNode.child = FindNeighbor(currentNode)
    if(len(currentNode.child) != 0):
        if(len(currentNode.child) == 1):
            currentNode.searched = True
        currentNode = currentNode.child.pop()
    for i in stack:
        if (i.state == currentNode.state):
            isInStack = True
            
    if (isInStack):
        currentNode = currentNode.parent
    else:
        stack.append(currentNode)
    if currentNode.searched:
        currentNode = currentNode.parent
        stack.pop()
    print(count)
    count = count + 1
    
    isInStack = False
    
        
    
    
#將路徑加入path
path = []
while currentNode != None:
    path.append(currentNode)
    currentNode = currentNode.parent
    
#顯示路徑
a = 0
print("step:", len(path) - 1)
while len(path) != 0:
    a+=1
    node = path.pop()
    for col in range(0, gameTypeNum):
        print(node.state[col * gameTypeNum : col * gameTypeNum + 3])
    print()
print(a)
print("end")