dad = ['Petr', 'Denis']
son = [['Oleg', 'Artur']]
answer = input("Enter Son's name: ")

if answer in son[0]:
    son[0].index(answer)
    print(dad[0])

input('Press enter')