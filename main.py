# main.py - "driver" code

import tree_node
import Problem
import Puzzle_GUI
from heapq import heappop, heappush
import math

# Calculates the uniform cost of a node from the inital node
# node: the node to check
def calculate_uniform_cost(node):
    return node.get_depth()         # returns depth of node

# Calculates the misplace tile heuristic of a node from the goal
# node: the node to check
def calculate_misplaced_tile(node):
    cost = 0
    tile_num = 0
    curr_state = node.get_state()

    # j = x coordinate of where the tile should be
    # i = y coordinate of where the tile should be
    for i in range(3):
        for j in range(3):
            if not(i == 2 and j == 2):              # do not calculate heurisitc for blank tile
                tile_num += 1
                idx = curr_state.index(tile_num)
                x = idx % 3                         # x = x coordinate of where the tile actually is
                y = idx // 3                        # y = y coordinate of where the tile actually is
                cost += abs(x-j) + abs(y-i)         # manhattan distance formula
    return cost

# Calculates euclidean distance of a node from the goal
# node: the tree node to check
def calculate_euclidean_dist(node):
    cost = 0
    tile_num = 0
    curr_state = node.get_state()

    # j = x coordinate of where the tile should be
    # i = y coordinate of where the tile should be
    for i in range(3):
        for j in range(3):
            if not(i == 2 and j == 2):              # do not calculate heurisitc for blank tile
                tile_num += 1
                idx = curr_state.index(tile_num)
                x = idx % 3                         # x = x coordinate of where the tile actually is
                y = idx // 3                        # y = y coordinate of where the tile actually is
                cost += math.sqrt(math.pow(abs(x-j), 2) + math.pow(abs(y-i), 2))    # distance formula

    return cost

# Checks if a state is unexplored by comparing the state to
# nodes in the explored nodes array and the frontier queue
#
# state_to_check:   the state to check
# explored_nodes:   array of explored nodes
# frontier:         queue of nodes in the frontier
def is_unexplored(state_to_check, explored_nodes, frontier, search_type):
    if search_type == "uniform_cost":
        for node in frontier:
            if state_to_check == node.get_state():
                return False
    else:
        for item in frontier:
            if state_to_check == item[1].get_state():
                return False

    for node in explored_nodes:
        if state_to_check == node.get_state():
            return False
    return True

# Returns unexplored children of the node by applying operator 
# functions from the Problem object to the state of the node
#
# node:             tree node that represents the state to expand
# problem:          object of Problem class with operator functions
# explored_nodes:   array of explored nodes
# frontier:         queue of nodes in the frontier
def expand_node(node, problem, explored_nodes, frontier, search_type):
    state_l = problem.move_left(node.get_state()[:])        # pass a copy of the state to move_left()  and store result in state_l
    state_r = problem.move_right(node.get_state()[:])       # pass a copy of the state to move_right() and store result in state_r
    state_u = problem.move_up(node.get_state()[:])          # pass a copy of the state to move_up()    and store result in state_u
    state_d = problem.move_down(node.get_state()[:])        # pass a copy of the state to move_down()  and store result in state_d
    unexplored_nodes = []

    if is_unexplored(state_l, explored_nodes, frontier, search_type):        # check if state_l is unexplored
        unexplored_nodes.append(tree_node.tree_node(state_l))
    if is_unexplored(state_r, explored_nodes, frontier, search_type):        # check if state_r is unexplored
        unexplored_nodes.append(tree_node.tree_node(state_r))
    if is_unexplored(state_u, explored_nodes, frontier, search_type):        # check if state_u is unexplored
        unexplored_nodes.append(tree_node.tree_node(state_u))
    if is_unexplored(state_d, explored_nodes, frontier, search_type):        # check if state_d is unexplored
        unexplored_nodes.append(tree_node.tree_node(state_d))

    return unexplored_nodes

# Searches for solution and returns the solution node
# problem:      object of Problem class with initial and goal state
# search_type:  "uniform_cost" for uniform cost search
#               "misplaced_tile" for misplaced tile heuristic
#               "eucilidean_dist" for euclidean distance heuristic
def search(problem, search_type):
    max_frontier_length = 1                                             # define a counter to keep track of the max number of nodes in the frontier queue
    frontier = []                                                       # define an empty frontier queue
    explored_nodes = []                                                 # define an array to keep track of all explored nodes
    initial_node = tree_node.tree_node(problem.get_initial_state())     # initialize a tree node to represent the inital state

    # add initial node to the frontier queue
    if search_type == "uniform_cost":                                   
        frontier.append(initial_node)                                   # use FIFO for uniform cost search                           
    else:
        heappush(frontier, (1, initial_node))                           # use priority queue for heuristic search

    print("Expanding State:")
    initial_node.print_state()
    print()

    # run till frontier queue is empty
    while(frontier):

        # pop node out of frontier queue
        if search_type == "uniform_cost":
            curr_node = frontier.pop(0)                          
        else:
            curr_node = heappop(frontier)[1]

        if curr_node.get_state() != initial_node.get_state():
            print("\nThe best state to expand with g(n) =", curr_node.get_cost_g(), "and h(n) =", curr_node.get_cost_h(), "is...")
        
        # check if the node is the solution
        if problem.is_solution(curr_node.get_state()):
            curr_node.print_state()
            print("\nReached Goal!\n")
            print("The search algorithm expanded", len(explored_nodes), "nodes")
            print("The maximum number of nodes in the queue at any one time:", max_frontier_length)
            print("Depth of the goal node is:", curr_node.get_cost_g(), "\n")
            return curr_node

        if curr_node.get_state() != initial_node.get_state():
            curr_node.print_state()
            print("Expanding this node...")

        # expand the node
        explored_nodes.append(curr_node)                                                            # add the node to the explored nodes array
        children_nodes = expand_node(curr_node, problem, explored_nodes, frontier, search_type)     # call expand_node() to get children of the node
        curr_node.add_children(children_nodes)                                                      # add children of the node to the search tree        

        # enqueue the children of the node into the frontier queue
        if search_type == "uniform_cost":
            for i in children_nodes:
                i.set_cost_g(calculate_uniform_cost(i))
                i.set_cost_h(0)
                frontier.append(i)
        elif search_type == "misplaced_tile":
            for i in children_nodes:
                cost_g = calculate_uniform_cost(i) 
                cost_h = calculate_misplaced_tile(i)
                i.set_cost_g(cost_g)
                i.set_cost_h(cost_h)
                heappush(frontier, (cost_g+cost_h, i))
        elif search_type == "euclidean_dist":
            for i in children_nodes:
                cost_g = calculate_uniform_cost(i) 
                cost_h = calculate_euclidean_dist(i)
                i.set_cost_g(cost_g)
                i.set_cost_h(cost_h)
                heappush(frontier, (cost_g+cost_h, i))
        
        # update the maximum number of nodes in the frontier
        if max_frontier_length < len(frontier):
            max_frontier_length = len(frontier)

    print("\nDid not reach goal")
    print("The search algorithm expanded", len(explored_nodes), "nodes")
    print("The maximum number of nodes in the queue at any one time:", max_frontier_length)

    return None

gui = Puzzle_GUI.Puzzle_GUI()
if gui.run():
    solution_node = search(gui.get_problem(), gui.get_heuristic())          # call search() to find the solution node
    if solution_node:                                                       # print the solution path
        print("Final Solution Path:")
        solution_node.print_solution_path()
