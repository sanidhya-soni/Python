a = 5
s = f"Your number is {a}"
print(s)
print(type(s))

# To print a paragraph we can enclose our string inside ''' ''' or """ """
print('''Haha
What Happened
This is the way we can type a paragraph''')

# Random module
import random
a = random.randint(1, 10)
b = random.random()
print(f"{a} {b}")

# Shuffle a List
cars = ['Aston Martin', 'Audi', 'BMW','Mercedes']
random.shuffle(cars)
print(cars)
