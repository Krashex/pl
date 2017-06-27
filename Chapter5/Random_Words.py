import random

printed_word = []

WORDS = ['Game', 'Name', "Fame", "Blame", "Flame", "Artur", "Anton", "Cola", "Hola"]
while len(printed_word) != len(WORDS):
    word = random.choice(WORDS)
    if word in printed_word:
        continue
    else:
        print(word)
        printed_word += [word]
