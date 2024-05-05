import heapq as hp


def in_goal_state(node):
    count = 1
    size = len(node)
    for i in range(0,size):
        for j in range(0,size):
            if node[i][j] != count and i != size-1 and j != size-1:
                return False
            elif i == size-1 and j == size-1 and node[i][j] != 0:
                return False
            count += 1
    return True

def queueing_function(heap, nodes):
    pass

def expand(node):
    pass


def general_search(problem):
    nodes = []
    hp.heappush(nodes, problem)
    while True:
        if len(nodes) <= 0:
            return -1 # failure
        node = hp.heappop(nodes)       
        if in_goal_state(node):
            return node
        nodes = queueing_function(nodes, expand(node))
        


general_search([[1,2,3], [4,5,6], [7,8,0]])
print(in_goal_state([[1,2,3], [4,5,6], [7,8,0]]))
