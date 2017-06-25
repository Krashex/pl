import random

COUNT_TRY = 10

guess = 0
x = random.randint(1, 2)
ans = -1

while guess <COUNT_TRY or ans != x:
    ans = int(input('Gues '))
    if ans != x:
        guess += 1
else:
    print("you lost")

print('You won')
input('нажмите Enter')
