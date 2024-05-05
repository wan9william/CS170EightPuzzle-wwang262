# Search Class the "driver" code with the search algorithms
import Problem
import tree_node
SIZE = 3


# Checks if a state is unexplored by comparing the state to
# nodes in the explored nodes array and the frontier queue
#
# state_to_check:   the state to check
# explored_nodes:   array of explored nodes
# frontier:         queue of nodes in the frontier
def is_unexplored(state_to_check, explored_nodes, frontier):
    node_list = explored_nodes + frontier
    for node in node_list:
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
def expand_node(node, problem, explored_nodes, frontier):
    state_l = problem.move_left(
        node.get_state()[:])  # pass a copy of the state to move_left()  and store result in state_l
    state_r = problem.move_right(
        node.get_state()[:])  # pass a copy of the state to move_right() and store result in state_r
    state_u = problem.move_up(
        node.get_state()[:])  # pass a copy of the state to move_up()    and store result in state_u
    state_d = problem.move_down(
        node.get_state()[:])  # pass a copy of the state to move_down()  and store result in state_d
    unexplored_nodes = []

    if is_unexplored(state_l, explored_nodes, frontier):  # check if state_l is unexplored
        unexplored_nodes.append(tree_node.tree_node(SIZE, state_l))
    if is_unexplored(state_r, explored_nodes, frontier):  # check if state_r is unexplored
        unexplored_nodes.append(tree_node.tree_node(SIZE, state_r))
    if is_unexplored(state_u, explored_nodes, frontier):  # check if state_u is unexplored
        unexplored_nodes.append(tree_node.tree_node(SIZE, state_u))
    if is_unexplored(state_d, explored_nodes, frontier):  # check if state_d is unexplored
        unexplored_nodes.append(tree_node.tree_node(SIZE, state_d))

    return unexplored_nodes


# Searches for solution and returns the solution node
# problem: object of Problem class with initial and goal state
def search(problem):
    root = tree_node.tree_node(SIZE,
                               problem.get_initial_state())  # initialize root of search tree with initial state
    frontier = [root]  # initialize the frontier queue with initial state
    explored_nodes = []  # array to keep track of all explored nodes

    while frontier:  # run till frontier queue is empty
        node = frontier.pop(0)  # pop node out of frontier queue
        if problem.is_solution(node.get_state()):  # check if the node is the solution
            print("reached goal")  # MUST REMOVE
            return node
        explored_nodes.append(node)  # add the node to the explored nodes array
        unexplored_nodes = expand_node(node, problem, explored_nodes,
                                            frontier)  # call expand_node() to get new unexplored nodes
        node.add_children(unexplored_nodes)  # update search tree with the unexplored nodes
        for i in unexplored_nodes:  # queue the unexplored nodes
            frontier.append(i)
