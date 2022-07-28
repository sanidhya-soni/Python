import random

# Example of List
a = ["Apple", "Mango", "Papaya", "Watermelon", "Pear", "Peach", "Grapes"]
print(a)

# To print an element at particular index, following syntax is used
# To access data from the end we use -ve numbers
print(a[0], a[-1])

# Taking input of a comma seperated string and storing values seperated by comma in list.
s = "Movie, Mall, Garden, Long Drive"
x = s.split(", ")
print(x)
print(random.choice(x))

# Nested List
cars = ["Audi", "BMW", "Mercedes", "Aston Martin", "Lamborghini"]
bikes = ["Royal Enfield", "BMW", "Yamaha"]
brands = [cars, bikes]
print(brands)
print(brands[0][3])
