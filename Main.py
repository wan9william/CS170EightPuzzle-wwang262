import Puzzle
import Solver



puzzle = Puzzle.Puzzle([1,0,2,4,5,3,7,8,6])
# puzzle.scramble(puzzle.startNode.state)
solver = Solver.Solver()
solver.general_search(puzzle)