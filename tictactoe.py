SIZE = 3  # both the winning line and (x, y) board size


def tic_tac_input(input_):
    input_ = input_.replace("_", " ")
    game_board = [[' '] * SIZE for _ in range(SIZE)]  # creates the 2D game board with empty cells
    for i in range(SIZE):
        game_board[i] = list(input_[i * SIZE: (i + 1) * SIZE])

    return game_board


grid = tic_tac_input(input())

print(f"""
      ---------\n
      | {' '.join(grid[0])} |\n
      | {' '.join(grid[1])} |\n
      | {' '.join(grid[2])} |\n
      ---------\n
      """)
