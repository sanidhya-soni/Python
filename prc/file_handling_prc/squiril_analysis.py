import pandas as pd

'''gray = 0
red = 0
black = 0

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

color = data['Primary Fur Color']

for i in color:
    if i == 'Gray':
        gray += 1
    elif i == 'Black':
        black += 1
    else:
        red += 1

new_data = {
    'Fur_Color': ['Red', 'Black', 'Gray'],
    'Count': [red, black, gray]
}

data = pd.DataFrame(new_data)
data.to_csv('Analyzed Squirrels')
print(data)'''

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

no_of_red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
no_of_black = len(data[data['Primary Fur Color'] == 'Black'])
no_of_gray = len(data[data['Primary Fur Color'] == 'Gray'])

new_data = {
    'Fur_Color': ['Cinnamon', 'Black', 'Gray'],
    'Count': [no_of_red, no_of_black, no_of_gray]
}

data = pd.DataFrame(new_data)
data.to_csv('Analyzed Squirrels')
print(data)
