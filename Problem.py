import random
import math

class Problem:
    def __init__(self,initialState):
        self.initialState = initialState.copy()
        self.currentState = initialState.copy()
        self.size = int(math.sqrt(len(self.initialState)))
    def left(self):
        x = self.currentState.index(0)
        if x % self.size != 0:
            temp = self.currentState[x - 1]
            self.currentState[x - 1] = self.currentState[x]
            self.currentState[x] = temp
    def right(self):
        x = self.currentState.index(0)
        if x % self.size != self.size-1:
            temp = self.currentState[x + 1]
            self.currentState[x + 1] = self.currentState[x]
            self.currentState[x] = temp
    def up(self):
        x = self.currentState.index(0)
        if x / self.size >= 1:
            temp = self.currentState[x - self.size]
            self.currentState[x - self.size] = self.currentState[x]
            self.currentState[x] = temp
    def down(self):
        x = self.currentState.index(0)
        if x / self.size < self.size:
            temp = self.currentState[x + self.size]
            self.currentState[x + self.size] = self.currentState[x]
            self.currentState[x] = temp
    def scramble(self):
        for x in range(0, random.randint(0, 1000)):
            temp_state = random.randint(0, 3)
            match temp_state:
                case 0:
                    self.left()
                case 1:
                    self.right()
                case 2:
                    self.up()
                case 3:
                    self.down()
    def check_solution(self):
        sizeSquared = self.size * self.size
        for x in range(0, sizeSquared):
            if (x != sizeSquared-1 and self.currentState[x] != x+1) or (x == sizeSquared-1 and self.currentState[x] != 0):
                return False
        return True
    def print_curr_state(self):
        a = self.currentState
        b = self.size
        for x in range(0, self.size*self.size,self.size):
            print(self.currentState[x:x+b])
        # print("\n")
        



def createInitState(size):
    return [x if x != size*size else 0 for x in range (1,size*size+1)]









p = Problem(createInitState(4))
# print(p.initialState)
print(p.check_solution())
p.left()
# p.left()
p.up()
p.up()
p.up()
p.up()
p.up()
p.up()
# p.up()
# print(p.check_solution())
p.print_curr_state()
print(p.size)

# print([x if x != 9 else 0 for x in range (1,10)])