import random
import math
import Node
import heapq as hp


def createGoalList(size):
    return [x if x != size*size else 0 for x in range (1,size*size+1)]


class Puzzle:
    def __init__(self,initialState):
        self.startNode = Node.Node(initialState.copy())
        self.size = int(math.sqrt(len(self.startNode.state)))
        self.goalNode = Node.Node(createGoalList(self.size))
    def expand(self, n): 
        nodes = []
        left = n.state.copy()
        right = n.state.copy()
        up = n.state.copy()
        down = n.state.copy()
        if self.left(left):
            newnode = Node.Node(left)
            newnode.lastAction = 1 # 1 = left, 2 = right, 3 = up, 4 = down
            newnode.parent = n
            nodes.append(newnode)
            n.addChild(newnode)
        if self.right(right):
            newnode = Node.Node(right)
            newnode.lastAction = 2 # 1 = left, 2 = right, 3 = up, 4 = down
            newnode.parent = n
            nodes.append(newnode)
            n.addChild(newnode)
        if self.up(up):
            newnode = Node.Node(up)
            newnode.lastAction = 3 # 1 = left, 2 = right, 3 = up, 4 = down
            newnode.parent = n
            nodes.append(newnode)
            n.addChild(newnode)
        if self.down(down):
            newnode = Node.Node(down)
            newnode.lastAction = 4 # 1 = left, 2 = right, 3 = up, 4 = down
            newnode.parent = n
            nodes.append(newnode)
            n.addChild(newnode)
        return nodes
            

    def left(self,state):
        x = state.index(0)
        if x % self.size != 0:
            temp = state[x - 1]
            state[x - 1] = state[x]
            state[x] = temp
            return True
        else:
            return False
    def right(self,state):
        x = state.index(0)
        if x % self.size != self.size-1:
            temp = state[x + 1]
            state[x + 1] = state[x]
            state[x] = temp
            return True
        else:
            return False
    def up(self,state):
        x = state.index(0)
        if x / self.size >= 1:
            temp = state[x - self.size]
            state[x - self.size] = state[x]
            state[x] = temp
            return True
        else:
            return False
    def down(self,state):
        x = state.index(0)
        if x + self.size <= self.size*self.size-1:
            temp = state[x + self.size]
            state[x + self.size] = state[x]
            state[x] = temp
            return True
        else:
            return False
    def scramble(self,state):
        for x in range(0, random.randint(0, 100)):
            temp_state = random.randint(0, 3)
            match temp_state:
                case 0:
                    self.left(state)
                case 1:
                    self.right(state)
                case 2:
                    self.up(state)
                case 3:
                    self.down(state)
    def check_solution(self,state):
        sizeSquared = self.size * self.size
        for x in range(0, sizeSquared):
            if (x != sizeSquared-1 and state[x] != x+1) or (x == sizeSquared-1 and state[x] != 0):
                return False
        return True
