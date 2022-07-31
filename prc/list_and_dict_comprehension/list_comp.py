ls = [1, 2, 3]
new_ls = [n + 1 for n in ls]
print(new_ls)

name = 'Sani'
new_name = [n for n in name]
print(new_name)

range_list = [2 * n for n in range(1, 11) if n % 2 == 0]
print(range_list)

names = ['Sanidhya', 'Prakhar', 'Mansi', 'Sharma', 'Alex']
big_names = [a.upper() for a in names if len(a) > 5]
print(big_names)
