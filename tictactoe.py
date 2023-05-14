SIZE = 3  # both the winning line and (x, y) board size


def tic_tac_input(input_):
    input_ = input_.replace("_", " ")
    game_board = [[' '] * SIZE for _ in range(SIZE)]  # creates the 2D game board with empty cells
    for i in range(SIZE):
        game_board[i] = list(input_[i * SIZE: (i + 1) * SIZE])

    return game_board


def tic_tac_print():
    print(f"""
          ---------\n
          | {' '.join(grid[0])} |\n
          | {' '.join(grid[1])} |\n
          | {' '.join(grid[2])} |\n
          ---------\n
          """)


grid = tic_tac_input(input())

tic_tac_print()

valid = False
while not valid:
    try:
        coordinates = [int(x) - 1 for x in input().split()]
    except ValueError:
        print("You should enter numbers!")
    else:
        if not (0 <= coordinates[0] <= 2 and 0 <= coordinates[1] <= 2):
            print("Coordinates should be from 1 to 3!")
        elif grid[coordinates[0]][coordinates[1]] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            valid = True
            grid[coordinates[0]][coordinates[1]] = "X"
            tic_tac_print()
