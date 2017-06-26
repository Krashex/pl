import random

WORDS = ("python", "game", "name", 'again', "interest", "house", "letter", "lesson")
word = random.choice(WORDS)
tries = 0
count_letters = len(word)
print("Tr1y to guess what the word is, you'll have five tries for guessing which letters does the word has.")
print('There is so many letters in word:', count_letters)
while tries < 5:
    letter = input('Type letter ')
    tries += 1
    if letter in word:
        print('Yes, this letter is in word')
    else:
        print('No,there is no this letter in word')

guess = input('Now try to guess the word: ')
if guess == word:
    print('You won. Congratulations!')
else:
    print('My apologise, You lost...')
