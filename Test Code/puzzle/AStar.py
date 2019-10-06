import RandomPuzzle as RP
class Node:
    def __init__(self, data, level, fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = None
    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x, y = self.find(self.data, 0)
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children
        
    def shuffle(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy(self,root):
            """ Copy function to create a similar matrix of the given node"""
            temp = []
            for i in root:
                t = []
                for j in i:
                    t.append(j)
                temp.append(t)
            return temp    
            
    def find(self, puz, x):
        """ Specifically used to find the position of the blank space """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j
class Puzzle:
    def __init__(self, puzzle):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = len(puzzle)
        self.open = []
        self.closed = []
        self.puzzle = puzzle
    def goal(self):
        temp = []
        goal = []
        for i in range(0, self.n):
            for j in range(1, self.n+1):
                temp = [k for k in range(1+i*self.n, self.n+1+i*self.n)]
            goal.append(temp)
        goal[self.n-1][self.n-1] = 0
        return goal
    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = self.puzzle[0+self.n*i:3+self.n*i]
            puz.append(temp)
        print(puz)    
        return puz
    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data, goal)+start.level
    def h(self, start, goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        
        for i in range(0, self.n):
            for j in range(0, self.n):
                for row in range(0, self.n):
                    if start[i][j] in goal[row]:
                        col = goal[row].index(start[i][j])
                        temp = temp + abs(row-i) + abs(col-j)
        
        """for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j]:
                    temp += 1"""
        return temp
    def stateInStates(self, state, states):
        for i in states:
            if state.data == i.data:
                return True
        return False
    def GetStateFromStates(self, state, states):
        for i in states:
            if state.data == i.data:
                return i
    def process(self):
        """ Accept Start and Goal Puzzle state"""
        #start = self.puzzle
        start = self.puzzle
        goal = self.goal()
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        """ Put the start node in the open list"""
        self.open.append(start)
        print("\n\n")
        #a = 0
        path = []
        cur = self.open[0]
        while(True):
            #a += 1
            #print(a)
            cur = self.open[0]
            if(self.h(cur.data, goal) == 0):
                break
            for i in cur.generate_child():
                i.parent = cur
                i.fval = self.f(i, goal)
                if self.stateInStates(i, self.closed):
                    continue
                if not self.stateInStates(i, self.open):
                    self.open.append(i)
                if self.stateInStates(i, self.open) and i.fval < self.GetStateFromStates(i, self.open).fval:
                    self.open.remove(self.GetStateFromStates(i, self.open))
                    self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            """ sort the opne list based on f value """
            self.open.sort(key=lambda x: x.fval, reverse=False)
            #for i in self.open:
               # print(i.data,i.fval,i.level)
        while(cur != start):
            path.append(cur)
            cur = cur.parent
        path.append(start)
        path.reverse()
        return path, len(path)


testMatrix = RP.RandomMatrix(3)
print(testMatrix.GetPuzzle())
print(testMatrix.GetStringPuzzle())
# puz = Puzzle(["7","6","1","3","2","8","4","5","0"])
puz = Puzzle(testMatrix.GetPuzzle())



path,steps = puz.process()
print(steps)
for step in path:
    for row in step.data:
        print(row)
    print()
