import heapq as hp
import Problem

exploredStates = dict()

def expand(problem, nodething):
    node = nodething[1]
    a = []
    left = node.copy()
    right = node.copy()
    up = node.copy()
    down = node.copy()
    if problem.left(left):
        a.append((1,left))
    if problem.right(right):
        a.append((1,right))
    if problem.up(up):
        a.append((1,up))
    if problem.down(down):
        a.append((1,down))
    return a


def queueing_function(heap, nodes):
    for i in range(0, len(nodes)):
        node = nodes[i]
        hp.heappush(heap, node)

def general_search(problem):
    nodes = []
    hp.heappush(nodes, (1,problem.initialState))
    while True:
        if len(nodes) <= 0:
            return -1 # failure
        node = hp.heappop(nodes)   
        # print(node)    
        # print(problem.check_solution(node[1]))
        print(node)
        print(problem.check_solution(node[1]))
        if problem.check_solution(node[1]):
            return node
        if str(node[1]) not in exploredStates:
            exploredStates[str(node[1])] = True
            queueing_function(nodes, expand(problem, node))
        

p = Problem.Problem(Problem.createInitState(3))
state = p.initialState
p.scramble(state)

general_search(p)
# print(str(state))
