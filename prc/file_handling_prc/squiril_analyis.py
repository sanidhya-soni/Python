import pandas as pd
gray = 0
red = 0
black = 0

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
for i in data['Primary Fur Color']:
    if i == 'Gray':
        gray += 1
    elif i == 'Cinnamon':
        red += 1
    elif i == 'Black':
        black += 1

sq_dict = {
    "Fur Colour": ['gray', 'red', 'black'],
    "count": [gray, red, black]
}

df = pd.DataFrame(sq_dict)
print(df)
df.to_csv('color_data.csv')
