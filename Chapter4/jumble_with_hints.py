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
start = 0
end = 3
HINTS_COUNT = 3
points = 20
# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
               Welcom1e to Word Jumble!

       Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\n(If you don't have any guesses type HINT)Your guess: ")
while HINTS_COUNT != 0:
    if guess == "HINT":
        print(correct[start:end])
        start = end
        end += 2
        HINTS_COUNT -= 1
        guess = input('Your guess ')
        if guess == correct:
            print("That's it!  You guessed it!\n")
            points -= 10
            break
    elif guess == correct:
        print("That's it!  You guessed it!\n")
        break
    else:
        print("Sorry, that's not it.")
        guess = input("Your guess: ")

print("Thanks for playing.You have earned", points, "points")

input("\n\nPress the enter key to exit.")
