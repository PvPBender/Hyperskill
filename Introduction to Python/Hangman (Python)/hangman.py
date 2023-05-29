from random import choice


def hintify(to_guess):
    to_guess_hinted = to_guess[:3] + "-" * max(0, (len(to_guess) - 3))
    return to_guess_hinted


def main():
    words = ("python", "java", "swift", "javascript")

    to_guess = choice(words)

    print("H A N G M A N")
    if input(f"Guess the word {hintify(to_guess)}: ") == to_guess:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
