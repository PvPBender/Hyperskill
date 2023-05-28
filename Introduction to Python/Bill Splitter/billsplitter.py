from random import choice


def main():
    print("Enter the number of friends joining (including you):")
    if (friends_num := int(input())) <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = [input() for _ in range(friends_num)]

        print("Enter the total bill value:")
        bill = int(input())

        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        if (answer := input()) != "Yes":
            print("No one is going to be lucky")
        else:
            lucky_one = choice(friends)
            print(f"{lucky_one} is the lucky one!")
            friends_num -= 1

        split_bill = round(bill / friends_num, 2)
        friends_bill = {friend: split_bill for friend in friends}
        if answer == "Yes":
            friends_bill[lucky_one] = 0

        print(friends_bill)


if __name__ == "__main__":
    main()
