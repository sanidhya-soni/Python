n = int(input('Enter N : '))
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end = '')
    for j in range(1, 6):
        print('*', end = '')
    print()