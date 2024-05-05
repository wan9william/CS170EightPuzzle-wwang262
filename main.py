# main.py - "driver" code
import Search
import Problem
initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]


class GUI:
    # initialize GUI
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
            choice = input(":")
            if choice == "S" or choice == "s":
                if self.start_game():
                    break
            elif choice == "X" or choice == "x":

                break
            else:

                print("INVALID INPUT TRY AGAIN")

    #GUI Screen for game modes
    #TODO: Test exit and enter your own puzzle inputs
    def start_game(self):
        while True:
            print("ENTER GAME TYPE")
            print("1- Default")
            print("2- Enter your own puzzle")
            print("X- Return to Main Menu")

            choice = input(":")

            if choice == "1":
                self._problem = Problem.Problem(self._size,
                                                self._problem.scramble_board(self._problem.get_initial_state()[:]))
                return self.game()
            elif choice == "2":
                if self.enter_puzzle():
                    return self.game()
            elif choice == "X" or choice == "x":
                return False
            else:

                print("INVALID INPUT TRY AGAIN")

    #GUI screen to enter your own puzzle
    #TODO: test valid puzzles, test exit input, incorporate larger puzzles
    def enter_puzzle(self):
        new_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        while True:
            print("ENTER YOUR PUZZLE, use a zero to represent the blank")
            print("'X' TO RETURN TO PREVIOUS MENU ")
            for i in range(1, 4):
                puzzle1, puzzle2, puzzle3 = input('Enter the line ' + str(i) + ' of the puzzle: ').split()
                if (puzzle1 == "X" or puzzle2 == "X" or puzzle3 == "X"
                        or puzzle1 == "x" or puzzle2 == "x" or puzzle3 == "x"):
                    return False
                new_state[count] = int(puzzle1)
                new_state[count + 1] = int(puzzle2)
                new_state[count + 2] = int(puzzle3)
                count += 3

            self._problem = Problem.Problem(self._size, new_state)
            return True


    #game screen for user input or solving with search algo
    #TODO: incorporate the different search algos
    def game(self):
        while True:
            self._problem.print_board()
            if self._problem.is_solution(self._problem.get_initial_state()[:]):
                print("=============================================")
                print("Congratulations! You've completed the puzzle!")
                print("=============================================")
                print("ENTER ANY KEY TO RETURN TO MAIN MENU")
                choice = input(":")
                if choice == "X":
                    return False
                else:
                    return False
            print("[V] TO SOLVE [X] TO RETURN TO MAIN MENU  ")
            print("[W]UP   [A]LEFT  [S]DOWN  [D]RIGHT")
            choice = input(":")
            if choice == "W" or choice == "w":                  # move blank space up
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_up(self._problem.get_initial_state()[:]))
            elif choice == "A" or choice == "a":                # move blank space left
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_left(self._problem.get_initial_state()[:]))
            elif choice == "S" or choice == "s":                # move blank space down
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_down(self._problem.get_initial_state()[:]))
            elif choice == "D" or choice == "d":                # move blank space right
                self._problem = Problem.Problem(self._size,
                                                self._problem.move_right(self._problem.get_initial_state()[:]))
            elif choice == "V" or choice == "v":
                solution_node = Search.search(self._problem)    # call search() to find the solution node
                solution_node.print_solution_path()             # print the solution path
            elif choice == "X" or choice == "x":
                return False
            else:
                print("INVALID INPUT")


gui = GUI()
gui.run()
