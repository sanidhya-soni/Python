# Iterating in a List
cars = ["Mercedes", "Audi", "Aston Martin", "Audi", "Roll's Royce"]
for car in cars:
    print(car)

# Iteration in a range of 5 to 9
for i in range(5, 10):
    print(i)

# Iteration in a range of 0 to 12 at intervals of 3
for i in range(0, 13, 3):
    print(i)

# Use of ! operator
x = 5
while x != 10:
    print(x)
    x+=1

# 'not' can also be used with boolean
z = True
while z is not False:
    print(z)
    z = False
