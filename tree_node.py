# Definition for the tree_node class

# Using collections.deque for stack implementation
from collections import deque

class tree_node:
    # Initialization for tree_node object
    # _board_array: array that represents the state of the 8-puzzle board
    # _children:    array that represents the node's children
    # _parent:      node that represents the parent of the node
    def __init__(self, board_array):
        self._board_array = board_array
        self._children = []
        self._parent = None

    # Returns the array that represents the state of the 8-puzzle board
    # Usage: node.get_state()
    def get_state(self):
        return self._board_array

    # Returns the depth of the node by tracing back to the root
    # Usage: node.get_depth()
    def get_depth(self):
        depth = 0
        parent = self._parent
        while parent:
            parent = parent._parent
            depth += 1
        return depth

    # Adds the child node
    # child: the child node
    # Usage: parent_node.add_child(child_node)
    def add_child(self, child):
        self._children.append(child)
        child._parent = self

    # Adds child nodes by appending each child in the array
    # children: array of child nodes
    # Usage: parent_node.add_children([child_node1, child_node2, ...])
    def add_children(self, children):
        for child in children:
            self._children.append(child)
            child._parent = self

    # Prints the state of the node
    # tab: # of spaces from the left - for formatting (default is 0)
    # Usage: node.print_state() or node.print_state(i) where i is some integer
    def print_state(self, tab=0):
        for x in range(0, 3):
            print(("  "*tab) + str(self._board_array[3 * x]), self._board_array[3 * x + 1], self._board_array[3 * x + 2])
    
    # Prints the state of all the nodes in the tree
    # Note: Only for testing
    # Usage: root_node.print_tree()
    def print_tree(self):
        if self._parent:                                # base case
            print(("  "*self.get_depth()) + "|",)       # formatting the placement of '|' in the tree diagram 
        self.print_state(self.get_depth())               # prints node
        if self._children:
            for child in self._children:
                child.print_tree()                      # recursively calls print_tree() on all child nodes

    # Prints the solution path by pushing the nodes into a stack
    # then popping the nodes out of the stack to reverse the output
    #Usage: goal_node.print_solution_path()
    def print_solution_path(self):
        solution_stack = deque()
        curr_state = self
        # pushes nodes into the stack starting from the goal
        # state ending on the initial state (traces backwards)
        while curr_state:
            solution_stack.append(curr_state)
            curr_state = curr_state._parent
        # pops nodes out of the stack and prints the solution path
        while solution_stack:
            solution_stack.pop().print_state()
            print("\n", end="")

# Testing
# root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 0])

# child1 = tree_node([1, 2, 3, 4, 5, 6, 7, 0, 8])
# child2 = tree_node([1, 2, 3, 4, 5, 0, 7, 8, 6])
# root.add_children([child1, child2])

# child3 = tree_node([1, 2, 3, 4, 5, 6, 0, 7, 8])
# child4 = tree_node([1, 2, 3, 4, 0, 6, 7, 5, 8])
# child1.add_children([child3, child4])

# child5 = tree_node([1, 2, 0, 4, 5, 3, 7, 8, 6])
# child2.add_child(child5)

# print("tree:")
# root.print_tree()

# print("solution path with child5 = goal")
# child5.print_solution_path()

# print("solution path with root = goal")
# root.print_solution_path()
