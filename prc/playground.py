def addition(*args):
    a = [n for n in args]
    return sum(a)


print(addition(1, 2, 3, 4, 5))


def calculate(**kwargs):
    print(kwargs)


calculate(name='Sani', age=21, sex='male')
