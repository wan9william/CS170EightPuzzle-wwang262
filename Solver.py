import heapq as hp
import Puzzle

class Solver:
    def __init__(self):
        self.reset()
    def reset(self):
        self.pqcount = 1
        self.exploredStates = dict()
    def queueing_function(self, heap, nodes):
        for i in range(0, len(nodes)):
            self.pqcount+=1
            node = nodes[i]
            hp.heappush(heap, (self.pqcount,node))
    def general_search(self, puzzle):
        self.reset()
        nodes = []
        hp.heappush(nodes, (1,puzzle.startNode))
        while True:
            if len(nodes) <= 0:
                return -1 # failure
            node = hp.heappop(nodes)   
            print(node[1])
            if puzzle.check_solution(node[1].state):
                return node[1]
            if str(node[1]) not in self.exploredStates:
                self.exploredStates[str(node[1])] = True
                puzzle.expand(node[1])
                self.queueing_function(nodes, node[1].children)