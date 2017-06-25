# Считает за пользователя
start = int(input('Enter start of counting '))
end = int(input("Enter end of counting"))
interval = (int(input("Enter interval")))

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
