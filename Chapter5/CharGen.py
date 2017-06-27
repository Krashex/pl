pull = 30
Agility = 5
Strength = 5
Health = 5
Wisdom = 5
while not pull < 0 or pull == 0:
    Ans = input("Type skill to upgrade:'\n1 - Agility\n 2 - Health\n 3 - Strength\n 4 - Wisdom\n"
                "Want to take back some points type UNDO + skill ")
    number = int(input('Now type number of points you want to add or take back.'))
    if number > pull:
        print("Yoy can't add more than you have!")
        continue
    if Ans == "Agility":
        Agility += number
        pull -= number
    if Ans == "Strength":
        Strength += number
        pull -= number
    if Ans == "Health":
        Health += number
        pull -= number
    if Ans == "Wisdom":
        Wisdom += number
        pull -= number
    if Ans == "UNDO Agility":
        pull += number
        Agility -= number
    if Ans == "UNDO Strength":
        pull += number
        Strength -= number
    if Ans == "UNDO Health":
        pull += number
        Health -= number
    if Ans == "UNDO Wisdom":
        pull += number
        Wisdom -= number
    else:
        print('Smth went wrong, check the grammar.')
        continue
    print("Ag.: ", Agility, "HP :", Health, "Str.: ", Strength, "Wis.: ", Wisdom, "Pull:", pull)
input('Press Enter')
