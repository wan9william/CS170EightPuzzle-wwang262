import random
import math

class Problem:
    def __init__(self,initialState):
        self.initialState = initialState.copy()
        self.size = int(math.sqrt(len(self.initialState)))
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
        if x + self.size < self.size*self.size-1:
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
    def print_state(self,state):
        a = state
        b = self.size
        for x in range(0, self.size*self.size,self.size):
            print(state[x:x+b])
        



def createInitState(size):
    return [x if x != size*size else 0 for x in range (1,size*size+1)]


