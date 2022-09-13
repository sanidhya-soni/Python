from random import randrange
from datetime import timedelta
from random import randint
import pandas as pd
import numpy as np
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

# d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
# print(random_date(d1, d2))

def generator(datapoints,start_d,end_d,min_w,max_w):
    DATE = []
    weights = []
    # d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    # d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    d1 = datetime.strptime(start_d, '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime(end_d, '%m/%d/%Y %I:%M %p')
    for i in range(datapoints):
        temp = random_date(d1,d2)
        s = str(temp.day)+"-"+str(temp.month)+"-"+str(temp.year)
        DATE.append(s)
        n = randint(min_w,max_w)
        weights.append(n)
    d= {'Date':DATE,
        'Weight':weights}
    df = pd.DataFrame(d)
    df.to_csv('Data.csv',index=False)

# data_points = int(input("Enter the number of data points : "))
data_points = 5000

# start_d = input("Enter the start date : ")
start_d = '9/9/2022 12:00 AM'

# end_d = input("Enter the end date : ")
end_d = '9/13/2022 12:00 AM'

# min_w = int(input("Enter the minimum weight : "))
min_w = 100

# max_w = int(input("Enter the max weight : "))
max_w = 200

generator(data_points,start_d,end_d,min_w,max_w)