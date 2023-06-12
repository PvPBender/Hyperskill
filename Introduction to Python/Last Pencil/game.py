def get_pencil_num():
    print("How many pencils would you like to use:")
    while True:
        pencil_number = input()

        if pencil_number.isdigit():
            pencil_number = int(pencil_number)
        else:
            print("The number of pencils should be numeric")
            continue

        if pencil_number == 0:
            print("The number of pencils should be positive")
            continue

        return pencil_number


def select_name(player="John", bot="Jack"):
    selected_name = input(f"Who will be the first ({player}, {bot}):\n")

    if selected_name == player:
        return player, bot, True
    elif selected_name == bot:
        return bot, player, False
    elif selected_name not in (player, bot):
        print(f"Choose between {player} and {bot}")
        return select_name(player, bot)


def player_takes_pencil(pencil_num):
    while True:
        try:
            taken_pencils = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        if taken_pencils not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
            continue
        if taken_pencils > pencil_num:
            print("Too many pencils were taken")
            continue

        return taken_pencils


def bot_takes_pencil(pencil_num):
    match pencil_num % 4:
        case 0:
            print(3)
            return 3  # winning
        case 1:
            print(1)
            return 1  # losing
        case 2:
            print(1)
            return 1  # winning
        case 3:
            print(2)
            return 2  # winning


def main():
    pencil_num = get_pencil_num()
    player_1, player_2, player_first = select_name()

    for i in range(pencil_num + 1):
        if pencil_num == 0:
            if i % 2 == 0:
                print(f"{player_1} won")
            else:
                print(f"{player_2} won")
            break
        print("|" * pencil_num)
        if i % 2 == 0:
            print(f"{player_1}'s turn:\n")
            if player_first:
                pencil_num -= player_takes_pencil(pencil_num)
            else:
                pencil_num -= bot_takes_pencil(pencil_num)
        else:
            print(f"{player_2}'s turn:\n")
            if player_first:
                pencil_num -= bot_takes_pencil(pencil_num)
            else:
                pencil_num -= player_takes_pencil(pencil_num)


if __name__ == "__main__":
    main()
