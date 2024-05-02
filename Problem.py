# Definition for the Problem class

import tree_node
import random

class Problem:
    # Initialization for Problem object
    # _initial_state:   tree node that represents the initial state of the 8-puzzle board
    # _curr_state:      tree node that represents the current state of the 8-puzzle board - starts off as initial state
    # _goal_state:      tree node that represents the goal state of the 8-puzzle board
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self._curr_state = initial_state
        self._goal_state = tree_node.tree_node([1, 2, 3, 4, 5, 6, 7, 8, 0])

    # Returns the node that represents the initial state of the 8-puzzle board
    # Usage: problem.get_initial_state()
    def get_initial_state(self):
        return self._initial_state
    
    # Returns the node that represents the current state of the 8-puzzle board
    # Usage: problem.get_current_state()
    def get_current_state(self):
        return self._curr_state

    # Moves the blank space (0) to the left by 1 square
    # Precondition: blank space (0) must not be in the left-most column
    # Usage: problem.move_left()
    def move_left(self):
        x = self._curr_state.get_state().index(0)
        if x % 3 != 0:
            temp = self._curr_state.get_state()[x - 1]
            self._curr_state.get_state()[x - 1] = self._curr_state.get_state()[x]
            self._curr_state.get_state()[x] = temp

    # Moves the blank space (0) to the right by 1 square
    # Precondition: blank space (0) must not be in the right-most column
    # Usage: problem.move_right()
    def move_right(self):
        x = self._curr_state.get_state().index(0)
        if x % 3 != 2:
            temp = self._curr_state.get_state()[x + 1]
            self._curr_state.get_state()[x + 1] = self._curr_state.get_state()[x]
            self._curr_state.get_state()[x] = temp


    # Moves the blank space (0) up by 1 square
    # Precondition: blank space (0) must not be in the top-most row
    # Usage: problem.move_up()
    def move_up(self):
        x = self._curr_state.get_state().index(0)
        if x / 3 > 1:
            temp = self._curr_state.get_state()[x - 3]
            self._curr_state.get_state()[x - 3] = self._curr_state.get_state()[x]
            self._curr_state.get_state()[x] = temp


    # Moves the blank space (0) down by 1 square
    # Precondition: blank space (0) must not be in the bottom-most row
    # Usage: problem.move_down()
    def move_down(self):
        x = self._curr_state.get_state().index(0)
        if x / 3 < 2:
            temp = self._curr_state.get_state()[x + 3]
            self._curr_state.get_state()[x + 3] = self._curr_state.get_state()[x]
            self._curr_state.get_state()[x] = temp


    # Scrambles the board by doing 1000 random moves
    # Usage: problem.scramble_board()
    def scramble_board(self):
        for x in range(0, random.randint(0, 1000)):
            temp_state = random.randint(0, 3)
            match temp_state:
                case 0:
                    self.move_left()
                case 1:
                    self.move_right()
                case 2:
                    self.move_down()
                case 3:
                   self. move_up()

    # Compares current state with goal state to check if solution is found
    # Usage: problem.check_solution
    def check_solution(self):
        if self._curr_state.get_state() == self._goal_state.get_state():
            return True
        return False
        # for x in range(0, 9):
        #     print(x+1,":",self._cur_state[x])
        #     if (self._cur_state[x] != x+1) & (x == 9 & self._cur_state[x] != 0):
        #         return False
        # return True

#Testing

# initial_state = tree_node.tree_node([1, 2, 3, 4, 5, 6, 7, 0, 8])
# problem = Problem(initial_state)
# problem.get_current_state().print_state()
# print("\n", end="")

# problem.move_right()
# problem.get_current_state().print_state()
# print("\n", end="")

# if problem.check_solution():
#     print("Reached goal")
# else:
#     print("Did not reach goal")

# problem.move_down()
# problem.get_current_state().print_state()
# print("\n", end="")

# problem.move_down()
# problem.get_current_state().print_state()
# print("\n", end="")

# problem.scramble_board()
# problem.get_current_state().print_state()
# print("\n", end="")