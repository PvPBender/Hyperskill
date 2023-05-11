SIZE = 3  # both the winning line and (x, y) board size


def tic_tac_input(input_):
    game_board = [[' '] * SIZE for _ in range(SIZE)]  # creates the 2D game board with empty cells

    for i in range(SIZE):
        game_board[i] = list(input_[i * SIZE: (i + 1) * SIZE])

    return game_board


def check_game_validity(game_board):
    x_count = sum(row.count("X") for row in game_board)
    o_count = sum(row.count("O") for row in game_board)

    if abs(x_count - o_count) > 1:
        return False
    else:
        return True


def check_wins(game_board):
    x_o_wins = [0, 0]

    def check_rows(game_board):
        nonlocal x_o_wins
        for i in range(SIZE):
            for j in range(SIZE - 1):
                if game_board[i][j] == "_":
                    break
                if game_board[i][j] != game_board[i][j + 1]:
                    break
                if j == SIZE - 2:
                    if game_board[i][j] == "X":
                        x_o_wins[0] += 1
                    else:
                        x_o_wins[1] += 1

    def check_columns(game_board):
        nonlocal x_o_wins
        for j in range(SIZE):
            for i in range(SIZE - 1):
                if game_board[i][j] == "_":
                    break
                if game_board[i][j] != game_board[i + 1][j]:
                    break
                if i == SIZE - 2:
                    if game_board[i][j] == "X":
                        x_o_wins[0] += 1
                    else:
                        x_o_wins[1] += 1

    def check_diagonals(game_board):
        nonlocal x_o_wins
        for i in range(SIZE - 1):
            if game_board[i][i] == "_":
                break
            if game_board[i][i] != game_board[i + 1][i + 1]:
                break
            if i == SIZE - 2:
                if game_board[i][i] == "X":
                    x_o_wins[0] += 1
                else:
                    x_o_wins[1] += 1

        for i in range(SIZE - 1):
            if game_board[i][SIZE - 1 - i] == "_":
                break
            if game_board[i][SIZE - 1 - i] != game_board[i + 1][SIZE - 2 - i]:
                break
            if i == SIZE - 2:
                if game_board[i][SIZE - 1 - i] == "X":
                    x_o_wins[0] += 1
                else:
                    x_o_wins[1] += 1

    check_rows(game_board)
    check_columns(game_board)
    check_diagonals(game_board)
    return x_o_wins


grid = tic_tac_input(input())
x_o_wins = check_wins(grid)

print(f"""
      ---------\n
      | {' '.join(grid[0])} |\n
      | {' '.join(grid[1])} |\n
      | {' '.join(grid[2])} |\n
      ---------\n
      """)

if not check_game_validity(grid):
    print("Impossible")

elif (
        sum(row.count("_") for row in grid) > 0
        and sum(x_o_wins) == 0
):
    print("Game not finished")

elif (
        x_o_wins[0] > 0
        and x_o_wins[1] > 0
):
    print("Impossible")

elif x_o_wins[0] > 0:
    print("X wins")
elif x_o_wins[1] > 0:
    print("O wins")
else:
    print("Draw")
