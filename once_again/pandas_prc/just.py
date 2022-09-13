import numpy as np
import pandas as pd
# from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
print(obj2['a'])  # Selecting single value or set of values using index
obj2['d'] = 6
print(obj2)
print(obj2[['c', 'a', 'd']])
print(obj2[obj2 > 0])
print(obj2 * 20)
print(np.exp(obj2))
print('b' in obj2)  # Returns boolean value if this exists or not
print('e' in obj2)

# Creating a series using dictionary
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)  # In this case the index will be in sorted order
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

# For missing data isnull or notnull can be used
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())  # Can be used as instance methods also

# Arithmetic Operations
print(obj3)
print(obj4)
print(obj3 + obj4)
print()
# Giving index name and table name
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

# DataFrames

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# frame.index = [1, 2, 3, 4, 5, 6]  # Changing index of the frame
print(frame)
print(frame.head())  # Selects only first five rows for large dataframes

# Specify order of columns
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)

# Retrieving single column in a data frame
print(frame2['state'])
print(frame2.year)  # Both the ways it would work

print(frame2.loc['three'])
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2.debt = val
print(frame2)

# If we try assigning a column which dosent exists then it will be created
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern']  # used to delete a particular column like in a dictionary
print(frame2)
print(frame2.columns)

# Dataframe from nested dictionary
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)


