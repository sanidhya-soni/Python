# with open('weather_data.csv', mode='r') as file:
#     data = file.readlines()
# print(data)

# import csv
#
# temp = []
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#
# print(temp)

import pandas
data = pandas.read_csv('weather_data.csv')
ls = data['temp']

avg = sum(ls) / len(ls)
print(avg)
