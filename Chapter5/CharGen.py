pull = 30
char1 = 0
char2 = 0
char3 = 0
char4 = 0
skills = [char1, char2, char3, char4]
while not pull < 0:
    answer = int(input("""
    Type 1 - if you want to add points
    Type 2 - if you want to take points back
    Type 3 - if you want to see stats
    Type 4 - if you want to quit: """))
    if answer == 4:
        break
    elif answer == 1:
        points = int(input("Enter number of points you want to spend: "))
        if points > pull or points == 0:
            print("You cant add or remove more than you have!")
            continue
        choice = int(input("""
        Type 1 - if you want to add points in Agility
        Type 2 - if you want to add points in Health
        Type 3 - if you want to add points in Strength
        Type 4 - if you want to add points in Wisdom: """))
        if choice in range(1, 5):
            skills[choice - 1] += points
            pull -= points
        else:
            print("There is no such an option...")
    elif answer == 2:
        points = int(input('Enter number of points you want to take back: '))
        if pull + points > 30:
            print('Impossible')
            continue
        choice = int(input("""
        Type 1 - if you want to add points in Agility
        Type 2 - if you want to add points in Health
        Type 3 - if you want to add points in Strength
        Type 4 - if you want to add points in Wisdom: """))
        if choice in range(1, 5):
            skills[choice - 1] -= points
            pull += points
        else:
            print('There is no such an option...')
    elif answer == 3:
        print(skills, "You have this much", pull, " points")


