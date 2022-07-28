# import csv
#
# rows = []
#
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         rows.append(row)
#
# index = rows[0].index('temp')
#
# for i in range(1, len(rows)):
#     print(rows[i][index])

# import pandas as pd
# data = pd.read_csv('weather_data.csv')
# # print(data)
# temp = data['temp'].to_list()
# maximum = data.temp.max()
# print(data[data['temp'] == maximum])
# print(data[data.condition == 'Sunny'])
#
# monday = data[data.day == 'Monday']
# temperature = int(monday.temp) * 9 / 5 + 32
# print(temperature)


import pandas as pd

# Creating dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv('new_csv_file.csv')
