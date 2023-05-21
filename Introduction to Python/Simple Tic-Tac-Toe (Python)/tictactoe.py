def game_print():
    print(f"""
    ---------
    | {' '.join(grid[0])} |
    | {' '.join(grid[1])} |
    | {' '.join(grid[2])} |
    ---------
    """)


def enter_move(side):
    while True:
        input_ = input()
        if len(input_) != 3:
            print("The input must be in the format of Y X")
        else:
            try:
                coordinates = [int(x) - 1 for x in input_.split()]
            except ValueError:
                print("You should enter numbers!")
            else:
                if not (0 <= coordinates[0] <= 2 and 0 <= coordinates[1] <= 2):
                    print("Coordinates should be from 1 to 3!")
                elif grid[coordinates[0]][coordinates[1]] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    grid[coordinates[0]][coordinates[1]] = side
                    game_print()
                    return grid, coordinates


def check_row(player) -> bool:
    return all([True if cell == player else False for cell in grid[coordinates[0]]])


def check_column(player) -> bool:
    for i in range(3):
        if grid[i][coordinates[0]] != player:
            return False
    else:
        return True


def check_diagonals(player) -> bool:
    if grid[1][1] == player:
        if grid[0][0] == player and grid[2][2] == player:
            return True
        elif grid[0][2] == player and grid[2][0] == player:
            return True
        else:
            return False
    else:
        return False


def check_win(player) -> bool:
    if check_row(player):
        print(f"{player} wins")
        return True
    elif check_column(player):
        print(f"{player} wins")
        return True
    elif check_diagonals(player):
        print(f"{player} wins")
        return True
    else:
        return False


grid = [[' '] * 3 for _ in range(3)]  # creates the 2D game board with empty cells

game_print()

# GAME: 3 * 3 moves
for i in range(9):
    if i % 2 == 0:
        side = "X"
    else:
        side = "O"
    grid, coordinates = enter_move(side)
    if check_win(side):
        break
else:
    print("Draw")
