from random import choice

words = ("python", "java", "swift", "javascript")

print("H A N G M A N")
if input("Guess the word: ") == choice(words):
    print("You survived!")
else:
    print("You lost!")
