import random

MAX = 4
COUNT_TRY = 10


def generate_number():
    return random.randint(1, MAX)


def ask_number():
    response = None
    while response not in range(1, MAX, ):
        response = int(input('Gues '))
        if response not in range(1, MAX):
            print('Incorrect number')

    return response


def start_game():
    guesses = 0
    while guesses < COUNT_TRY:
        guesses += 1
        correct = generate_number()
        answer = ask_number()
        if answer == correct:
            print('You won')
            break

    if guesses == COUNT_TRY:
        print("you lost")


def main():
    start_game()
    input('нажмите Enter')


main()
