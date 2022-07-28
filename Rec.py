""" def power(a, x):
    if(x == 1):
        return a
    return a * power(a, x - 1)

print(power(10, 2))
 """


""" def sum(x):
    if(x == 0):
        return 0
    return x + sum(x - 1)

print(sum(int(input('Enter N : ')))) """


""" def feb(a, b, i):
    if(i == 0):
        return
    print(a + b, end = ' ')
    feb(b, a + b, i - 1)

feb(-1, 1, 20) """