import Puzzle
import Solver

puzzle = Puzzle.Puzzle([1,2,0,4,5,3,7,8,6])
# puzzle = Puzzle.Puzzle([1,2,3,4,5,6,7,0,8])
# puzzle.scramble(puzzle.startNode.state)
solver = Solver.Solver()
sol = solver.general_search(puzzle)
print(sol.getPath())
print(sol.depth)

st = puzzle.startNode
print(puzzle.startNode)

# puzzle.down(st.state)
# puzzle.down(st.state)
# print(puzzle.startNode)
# print(puzzle.down(st.state))