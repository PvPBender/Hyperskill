from random import choice
from string import ascii_lowercase


def play(wins, losses):
    to_guess = choice(("python", "java", "swift", "javascript"))
    to_guess_list = ['-' for _ in to_guess]
    guessed_letters = set()

    attempts = 8
    while attempts > 0:
        print('\n' + ''.join(to_guess_list))

        if len(letter := input("Input a letter: ")) != 1:
            print("Please, input a single letter.")
            continue
        elif letter not in ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        elif letter in guessed_letters:
            print("You've already guessed this letter.")

        guessed_letters.add(letter)

        if letter in to_guess:
            to_guess_list = [letter if x == letter else to_guess_list[i] for i, x in enumerate(to_guess)]

            if to_guess_list == list(to_guess):
                print(f"You guessed the word {to_guess}!\nYou survived!")
                wins += 1
                return wins, losses

        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1
            if attempts == 0:
                print("\nYou lost!")
                losses += 1
                return wins, losses


def results(wins, losses):
    print(f"You won: {wins} times.")
    print(f"You lost: {losses} times.")


def main():
    print("H A N G M A N")
    wins, losses = 0, 0

    while (command := input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')) != "exit":
        if command == "play":
            wins, losses = play(wins, losses)
        elif command == "results":
            results(wins, losses)
        else:
            print("Wrong command.")


if __name__ == "__main__":
    main()
