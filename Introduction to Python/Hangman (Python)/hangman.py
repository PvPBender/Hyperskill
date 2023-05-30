from random import choice

def main():
    print("H A N G M A N")

    to_guess = choice(("python", "java", "swift", "javascript"))
    to_guess_list = ['-' for _ in to_guess]
    to_guess_set = set(to_guess)

    attempts = 8
    for i in range(attempts):
        print('\n' + ''.join(to_guess_list))

        if (guessed := input("Input a letter: ")) in to_guess_set:
            to_guess_list = [guessed if x == guessed else to_guess_list[j] for j, x in enumerate(to_guess)]
        else:
            print("That letter doesn't appear in the word.")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
