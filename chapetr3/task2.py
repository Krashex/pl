import random

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
    answer = None
    count_try = 10
    guesses = 0
    while guesses < count_try:
        correct = number()
        answer = ask_number()
        if answer != correct:
            guesses += 1
        elif answer == correct:
            print('You won')
            break
    if guesses == count_try:
        print("you lost")


def main():
    checking()
    input('нажмите Enter')

main()
