# datareadclean.py
# this program read, print and save data as data frame
# Author: Fatima Zeino

import pandas as pd
import re

logFilename = 'access.log'

'''
df = pd.read_csv(logFilename, sep=' ', header=None)
#print(df)
print(df.iloc[0]) '''

colNames = ('ip',
    'userId',
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno'
    )

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

#df.drop(columns=['dash1', 'userId'], inplace=True)
#df['time']=df['time'].apply(lambda x: re.search('[\w:/+', x).group())
df['time']=pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print(df.iloc[0])
#print(df.dtypes)

