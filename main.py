# main.py - "driver" code
import tree_node
import Problem

initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]


class GUI:
    # initialize GU
    def __init__(self):
        self._size = 3
        self._problem = Problem.Problem(self._size, initial_state)

    # runs the main screen for the GUI
    def run(self):
        while True:
            print("WELCOME TO EIGHT PUZZLE SOLVER")
            print("BY ARYAN GOEL ANTHONY JOHNSON WILLIAM WANG")
            print("[S]START")
            print("[X]EXIT")
            choice = input()
            if choice == "S" or choice == "s":
                if self.start_game():
                    break
            elif choice == "X" or choice == "x":

                break
            else:

                print("INVALID INPUT TRY AGAIN")

    def start_game(self):
        while True:
            print("ENTER GAME TYPE")
            print("1- Default")
            print("2- Enter your own puzzle")
            print("X- Return to Main Menu")

            choice = input()

            if choice == "1":
                # self._problem = Problem.Problem(self._size,
                #                                self._problem.scramble_board(self._problem.get_initial_state()[:]))
                return self.game()
            elif choice == "2":
                if self.enter_puzzle():
                    return self.game()
            elif choice == "X" or choice == "x":
                return False
            else:

                print("INVALID INPUT TRY AGAIN")

    def enter_puzzle(self):
        new_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        while True:
            print("'X' TO RETURN TO PREVIOUS MENU ")
            for i in range(1, 3):
                puzzle1, puzzle2, puzzle3 = input('Enter the line ' + i + ' of the puzzle: ').split()
                if (puzzle1 == "X" or puzzle2 == "X" or puzzle3 == "X"
                        or puzzle1 == "x" or puzzle2 == "x" or puzzle3 == "x"):
                    return False
                new_state[count] = int(puzzle1)
                new_state[count + 1] = int(puzzle2)
                new_state[count + 2] = int(puzzle3)
                count += 3

            if self.valid_puzzle(new_state):
                self._problem.puzzle = Problem.Problem(self._size, new_state)
                return True
            else:
                print("INVALID INPUT TRY AGAIN")

    # Checks if a state is unexplored by comparing the state to
    # nodes in the explored nodes array and the frontier queue
    #
    # state_to_check:   the state to check
    # explored_nodes:   array of explored nodes
    # frontier:         queue of nodes in the frontier
    def is_unexplored(self, state_to_check, explored_nodes, frontier):
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
    def expand_node(self, node, problem, explored_nodes, frontier):
        state_l = problem.move_left(
            node.get_state()[:])  # pass a copy of the state to move_left()  and store result in state_l
        state_r = problem.move_right(
            node.get_state()[:])  # pass a copy of the state to move_right() and store result in state_r
        state_u = problem.move_up(
            node.get_state()[:])  # pass a copy of the state to move_up()    and store result in state_u
        state_d = problem.move_down(
            node.get_state()[:])  # pass a copy of the state to move_down()  and store result in state_d
        unexplored_nodes = []

        if self.is_unexplored(state_l, explored_nodes, frontier):  # check if state_l is unexplored
            unexplored_nodes.append(tree_node.tree_node(self._size, state_l))
        if self.is_unexplored(state_r, explored_nodes, frontier):  # check if state_r is unexplored
            unexplored_nodes.append(tree_node.tree_node(self._size, state_r))
        if self.is_unexplored(state_u, explored_nodes, frontier):  # check if state_u is unexplored
            unexplored_nodes.append(tree_node.tree_node(self._size, state_u))
        if self.is_unexplored(state_d, explored_nodes, frontier):  # check if state_d is unexplored
            unexplored_nodes.append(tree_node.tree_node(self._size, state_d))

        return unexplored_nodes

    # Searches for solution and returns the solution node
    # problem: object of Problem class with initial and goal state
    def search(self, problem):
        root = tree_node.tree_node(self._size,
                                   problem.get_initial_state())  # initialize root of search tree with initial state
        frontier = [root]  # initialize the frontier queue with initial state
        explored_nodes = []  # array to keep track of all explored nodes

        while frontier:  # run till frontier queue is empty
            node = frontier.pop(0)  # pop node out of frontier queue
            if problem.is_solution(node.get_state()):  # check if the node is the solution
                print("reached goal")  # MUST REMOVE
                return node
            explored_nodes.append(node)  # add the node to the explored nodes array
            unexplored_nodes = self.expand_node(node, problem, explored_nodes,
                                                frontier)  # call expand_node() to get new unexplored nodes
            node.add_children(unexplored_nodes)  # update search tree with the unexplored nodes
            for i in unexplored_nodes:  # queue the unexplored nodes
                frontier.append(i)

    def valid_puzzle(self, state):
        return True

    def game(self):
        while True:

            self._problem.print_board()
            print(self._problem.get_initial_state())
            print("[V] TO SOLVE [X] TO RETURN TO MAIN MENU  ")
            print("[W] SWAP UP  [A] SWAP LEFT [S] SWAP DOWN [D] SWAP RIGHT")
            choice = input()
            if choice == "W" or choice == "w":
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_up(self._problem.get_initial_state()[:]))
            elif choice == "A" or choice == "a":
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_left(self._problem.get_initial_state()[:]))
            elif choice == "S" or choice == "s":
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_down(self._problem.get_initial_state()[:]))
            elif choice == "D" or choice == "d":
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_right(self._problem.get_initial_state()[:]))
            elif choice == "V" or choice == "v":
                solution_node = self.search(self._problem)  # call search() to find the solution node
                solution_node.print_solution_path()  # print the solution path
                return False
            elif choice == "X" or choice == "x":
                return False
            else:
                print("INVALID INPUT")

            if self._problem.is_solution(self._problem.get_initial_state()[:]):
                print("Congratulations! You've got the puzzle!")
                print("PRESS ANY KEY TO RETURN TO MAIN MENU")
                choice = input()
                return False


gui = GUI()
gui.run()
