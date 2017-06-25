# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
points = 10
# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
               Welcome to Word Jumble!

       Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\n(If you don't have any guesses type HINT)Your guess: ")
if guess == "HINT":
    print(correct[0:3])
    guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it!  You guessed it!\n")
    points += 10

print("Thanks for playing.You have earned", points, "points")

input("\n\nPress the enter key to exit.")
