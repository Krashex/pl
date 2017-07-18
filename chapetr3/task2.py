import random

A = None
MAX = 4


def number():
    x = None
    x = random.randint(1, MAX)
    return x


def ask_number():
    response = None
    while response not in range(1, MAX, ):
        response = int(input('Gues '))
        if response not in range(1, MAX):
            print('Incorrect number')

    return response


def checking():
    COUNT_TRY = 10
    GUESSES = 0
    while GUESSES < COUNT_TRY:
        correct = number()
        A = ask_number()
        if A != correct:
            GUESSES += 1
        elif A == correct:
            print('You won')
            break
    if GUESSES == COUNT_TRY:
        print("you lost")


def main():
    checking()
    input('нажмите Enter')


main()
