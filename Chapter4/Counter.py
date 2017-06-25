# Считает за пользователя
start = int(input('Enter start of counting '))
end = int(input("Enter end of counting 1"))
interval = (int(input("Enter interval 1")))

if start > end:
    if interval > start - end:
        print("IT'S IMPOSSIBLE")
    else:
        for i in range(end, start, interval):
            print(i)
elif interval > end - start:
    print("IT'S IMPOSSIBLE!!!")
else:
    for i in range(start, end, interval):
        print(i)

input('press enter to quit')
