numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

names = ['Divyam', 'Sanidhya', 'Prakhar', 'Raj', 'Harry', 'Priyanshi']

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
