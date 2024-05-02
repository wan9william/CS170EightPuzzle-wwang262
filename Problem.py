# Definition for the Problem class

import random

class Problem:
    # Initialization for Problem object
    # _initial_state:   array that represents the initial state of the 8-puzzle board
    # _goal_state:      array that represents the goal state of the 8-puzzle board
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self._goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # Returns the node that represents the initial state of the 8-puzzle board
    # Usage: problem.get_initial_state()
    def get_initial_state(self):
        return self._initial_state

    # Moves the blank space (0) to the left by 1 square
    # Precondition: blank space (0) must not be in the left-most column
    # curr_state: the array that represents the state that is modified
    # Usage: problem.move_left(curr_state)
    def move_left(self, curr_state):
        x = curr_state.index(0)
        if x % 3 != 0:
            temp = curr_state[x - 1]
            curr_state[x - 1] = curr_state[x]
            curr_state[x] = temp
        return curr_state

    # Moves the blank space (0) to the right by 1 square
    # Precondition: blank space (0) must not be in the right-most column
    # curr_state: the array that represents the state that is modified
    # Usage: problem.move_right(curr_state)
    def move_right(self, curr_state):
        x = curr_state.index(0)
        if x % 3 != 2:
            temp = curr_state[x + 1]
            curr_state[x + 1] = curr_state[x]
            curr_state[x] = temp
        return curr_state

    # Moves the blank space (0) up by 1 square
    # Precondition: blank space (0) must not be in the top-most row
    # curr_state: the array that represents the state that is modified
    # Usage: problem.move_up(curr_state)
    def move_up(self, curr_state):
        x = curr_state.index(0)
        if x / 3 > 1:
            temp = curr_state[x - 3]
            curr_state[x - 3] = curr_state[x]
            curr_state[x] = temp
        return curr_state

    # Moves the blank space (0) down by 1 square
    # Precondition: blank space (0) must not be in the bottom-most row
    # curr_state: the array that represents the state that is modified
    # Usage: problem.move_down(curr_state)
    def move_down(self, curr_state):
        x = curr_state.index(0)
        if x / 3 < 2:
            temp = curr_state[x + 3]
            curr_state[x + 3] = curr_state[x]
            curr_state[x] = temp
        return curr_state

    # Scrambles the board by doing 1000 random moves
    # curr_state: the array that represents the state that is modified
    # Usage: problem.scramble_board(curr_state)
    def scramble_board(self, curr_state):
        for x in range(0, random.randint(0, 1000)):
            temp_state = random.randint(0, 3)
            match temp_state:
                case 0:
                    self.move_left(curr_state)
                case 1:
                    self.move_right(curr_state)
                case 2:
                    self.move_down(curr_state)
                case 3:
                   self. move_up(curr_state)
        return curr_state

    # Compares with goal state to check if solution is found
    # state_to_check: array that represents the state to compares with the goal state
    # Usage: problem.is_solution(state_to_check)
    def is_solution(self, state_to_check):
        if state_to_check == self._goal_state:
            return True
        return False
        # for x in range(0, 9):
        #     print(x+1,":",self._cur_state[x])
        #     if (self._cur_state[x] != x+1) & (x == 9 & self._cur_state[x] != 0):
        #         return False
        # return True