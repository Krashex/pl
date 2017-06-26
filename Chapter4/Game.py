import random

WORDS = ("python", "game", "name", 'again', "interest", "house", "letter", "lesson")
word = random.choice(WORDS)
tries = 0
count_letters = len(word)
print("Try to guess the word, you'll have five tries to guess which letters the word consists of.")
print('There is so many letters in word:', count_letters)
while tries < 5:
    letter = input('Type letter(If you think you now enough letters to guess the word type: GUESS) ')
    if letter == "GUESS":
        break
    if len(letter) > 1:
        print('You entered more than one symbol.Try to play fair!')
        continue
    tries += 1
    if letter in word:
        print('Yes, this letter is in word.')
    else:
        print('No,there is no this letter in word.')

guess = input('Now try to guess the word: ')
if guess == word:
    print('You won. Congratulations!')
else:
    print('My apologise, You lost...')
