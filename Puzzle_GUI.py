import tree_node
import Problem

class Puzzle_GUI:

    def __init__(self):
        self._problem = Problem.Problem([1,2,3,4,5,6,7,8,0])

    def get_problem(self):
        return self._problem
    
    def get_heuristic(self):
        while True:
            print("Enter your choice of algorithm")
            print("1: Uniform Cost Search")
            print("2: A* with the Misplaced Tile heuristic")
            print("3: A* with the Euclidean distance heuristic")
            heuristic = input()

            if int(heuristic) == 1:
                return "uniform_cost"
            if int(heuristic) == 2:
                return "misplaced_tile"
            if int(heuristic) == 3:
                return "euclidean_dist"
            else:
                print("INVALID INPUT TRY AGAIN")

    # runs the main screen for the GUI
    def run(self):
        while True:
            print("WELCOME TO EIGHT PUZZLE SOLVER")
            print("BY ARYAN GOEL (862134846) ANTHONY JOHNSON (862315881) WILLIAM WANG (862323453)")
            print("[S]START")
            print("[X]EXIT")
            choice = input()
            if choice == "S" or choice == "s":
                if self.start_game():
                    return True
            elif choice == "X" or choice == "x":
                return False
            else:
                print("INVALID INPUT TRY AGAIN")

    # GUI Screen for game modes
    def start_game(self):
        while True:
            print("ENTER GAME TYPE")
            print("1- Default")
            print("2- Enter your own puzzle")
            print("X- Return to Main Menu")

            choice = input()

            if choice == "1":
                initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
                self._problem = Problem.Problem(initial_state)          # initialize problem object with initial state
                self._problem.scramble_board(initial_state)             # scramble the initial state of the problem
                return True
            elif choice == "2":
                initial_state = self.enter_puzzle()
                if initial_state:
                    return self.game(initial_state)
            elif choice == "X" or choice == "x":
                return False
            else:
                print("INVALID INPUT TRY AGAIN")

    #GUI screen to enter your own puzzle
    #TODO: test valid puzzles, test exit input, incorporate larger puzzles
    def enter_puzzle(self):
        new_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        print("ENTER YOUR PUZZLE, use a zero to represent the blank")
        for i in range(1, 4):
            puzzle1, puzzle2, puzzle3 = input('Enter the line ' + str(i) + ' of the puzzle (please seperate #s by a [space]): ').split()
            new_state[count] = int(puzzle1)
            new_state[count + 1] = int(puzzle2)
            new_state[count + 2] = int(puzzle3)
            count += 3

        return new_state

    #game screen for user input or solving with search algo
    #TODO: incorporate the different search algos
    def game(self, initial_state):
        while True:
            self._problem = Problem.Problem(initial_state)
            print("The puzzle you have chosen is:")
            tree_node.tree_node(self._problem.get_initial_state()).print_state()
            print("[V] TO SOLVE [X] TO RETURN TO MAIN MENU  ")
            print("[W] SWAP UP  [A] SWAP LEFT [S] SWAP DOWN [D] SWAP RIGHT")
            choice = input()
            if choice == "W" or choice == "w":
                self._problem.move_up(initial_state)
            elif choice == "A" or choice == "a":
                self._problem.move_left(initial_state)
            elif choice == "S" or choice == "s":
                self._problem.move_down(initial_state)
            elif choice == "D" or choice == "d":
                self._problem.move_right(initial_state)
            elif choice == "V" or choice == "v":
                return True
            elif choice == "X" or choice == "x":
                return False
            else:
                print("INVALID INPUT")
