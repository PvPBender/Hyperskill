from random import choice


def main():
    print("H A N G M A N")

    to_guess = choice(("python", "java", "swift", "javascript"))
    to_guess_list = ['-' for _ in to_guess]
    to_guess_set = set(to_guess)

    attempts = 8
    while attempts > 0:
        print('\n' + ''.join(to_guess_list))

        if (guessed := input("Input a letter: ")) in to_guess_set:
            if guessed in to_guess_list:
                print("No improvements.")
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    break

            else:
                to_guess_list = [guessed if x == guessed else to_guess_list[i] for i, x in enumerate(to_guess)]

                if to_guess_list == list(to_guess):
                    print(f"\n{to_guess}\nYou guessed the word!\nYou survived!")
                    break

        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1
            if attempts == 0:
                print("You lost!")
                break


if __name__ == "__main__":
    main()
