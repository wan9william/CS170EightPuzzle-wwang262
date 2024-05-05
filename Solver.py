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
            hp.heappush(heap, (node.depth, self.pqcount,node))
    def general_search(self, puzzle):
        self.reset()
        nodes = []
        hp.heappush(nodes, (1,0,puzzle.startNode))
        while True:
            if len(nodes) <= 0:
                return -1 # failure
            node = hp.heappop(nodes)   
            print(node[2])
            if puzzle.check_solution(node[2].state):
                return node[2]
            if str(node[2]) not in self.exploredStates:
                self.exploredStates[str(node[2])] = True
                puzzle.expand(node[2])
                self.queueing_function(nodes, node[2].children)