import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def my_function():
    print("Hello World!")


def print_board():
    for x in range(0, 3):
        print(board[3 * x], board[3 * x + 1], board[3 * x + 2])
    print("\n")


def move_left():
    x = board.index(0)
    if x % 3 != 0:
        temp = board[x - 1]
        board[x - 1] = board[x]
        board[x] = temp


def move_right():
    x = board.index(0)
    if x % 3 != 2:
        temp = board[x + 1]
        board[x + 1] = board[x]
        board[x] = temp


def move_up():
    x = board.index(0)
    if x / 3 > 1:
        temp = board[x - 3]
        board[x - 3] = board[x]
        board[x] = temp


def move_down():
    x = board.index(0)
    if x / 3 < 2:
        temp = board[x + 3]
        board[x + 3] = board[x]
        board[x] = temp


def scramble_board():
    for x in range(0, random.randint(0, 1000)):
        temp_state = random.randint(0, 3)
        match temp_state:
            case 0:
                move_left()
            case 1:
                move_right()
            case 2:
                move_down()
            case 3:
                move_up()


def check_solution():
    for x in range(0, 9):
        if board[x] != x+1 & board[x] != 0:
            return False
    return True


print_board()
move_left()
print_board()
move_left()
print_board()
move_left()
print_board()
move_right()
print_board()
move_right()
print_board()
move_right()
print_board()
move_up()
print_board()
move_up()
print_board()
move_up()
print_board()
move_down()
print_board()
move_down()
print_board()
move_down()
print_board()
move_up()
print_board()
move_left()
print_board()
scramble_board()
print_board()
