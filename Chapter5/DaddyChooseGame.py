pairs = {'Oleg': 'Petr',
         'Artur': 'Denis',
         'Ivan': 'Petr'}
choice = None
print("""
                Type 1 - if you want to know smb's father's name
                Type 2 - if you want to add new pairs
                Type 3 - if you want to remove sm pair
                Type 4 - if you want to change sm pair
                Type 5 - if you want to show all pairs
                Type 6 - if you want to see the table
                Type 7 - if you want to quit.
                 P.S. Be careful and don't give same names to sons!""")
while choice != 7:
    choice = int(input('Type number: '))
    if choice == 1:
        answer = input("Type son's name: ")
        if answer not in pairs:
            print('There is no such a name, if you want to add pair press 2')
        else:
            print(pairs[answer], 'is the', answer + "'s", 'father')
    elif choice == 2:
        new_son = input("Type new son's name: ")
        new_father = input("Type new father's name: ")
        pairs[new_son] = new_father
    elif choice == 3:
        print("Type son's name and you'll delete pair with this son")
        removed = input('Enter name: ')
        if removed in pairs:
            del pairs[removed]
        else:
            print("There is no such a name...")
    elif choice == 4:
        change = input("Type son's name in pair that you want to change: ")
        if change in pairs:
            new_name = input("Now type new father's name: ")
            pairs[change] = new_name
        else:
            print("There is no such a name...")

    elif choice == 5:
        for item in pairs.items():
            print(item[0] + " " + item[1])
    elif choice == 6:
        print("""
                Type 1 - if you want to know smb's father's name
                Type 2 - if you want to add new pairs
                Type 3 - if you want to remove sm pair
                Type 4 - if you want to change sm pair
                Type 5 - if you want to show all pairs
                Type 6 - if you want to see the table
                Type 7 - if you want to quit.
                 P.S. Be careful and don't give same names to sons!""")
    elif choice == 7:
        break
    else:
        print("There is no such a number...")
