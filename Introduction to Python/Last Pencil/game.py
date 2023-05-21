import string  # I would just use isdigit(), but I have to use the string module


def get_pencil_num():
    print("How many pencils would you like to use:")
    while True:
        pencil_number = input()

        if all(char in string.digits for char in pencil_number):
            pencil_number = int(pencil_number)
        else:
            print("The number of pencils should be numeric")
            continue

        if pencil_number == 0:
            print("The number of pencils should be positive")
            continue

        return pencil_number


def select_name(name_1="John", name_2="Jack"):
    selected_name = input(f"Who will be the first ({name_1}, {name_2}):\n")

    if selected_name == name_1:
        return name_1, name_2
    elif selected_name == name_2:
        return name_2, name_1
    elif selected_name not in (name_1, name_2):
        print(f"Choose between {name_1} and {name_2}")
        return select_name(name_1, name_2)


def get_taken_pencils(pencil_num):
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


def main():
    pencil_num = get_pencil_num()

    name_1, name_2 = select_name()

    for i in range(pencil_num):
        if pencil_num == 0:
            if i % 2 == 0:
                print(f"{name_1} won")
            else:
                print(f"{name_2} won")
            break
        print("|" * pencil_num)
        if i % 2 == 0:
            print(f"{name_1}'s turn:\n")
        else:
            print(f"{name_2}'s turn:\n")

        pencil_num -= get_taken_pencils(pencil_num)


if __name__ == "__main__":
    main()
