# dataframeinout.py
# this program print and save data as data frame
# Author: Fatima Zeino

import pandas as pd 

listdata = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIem', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'Math', 73],
    ['John', 'programming', 61]
]
df = pd.DataFrame(listdata, columns=['name', 'subject', 'grade'])
print(df.head(3))
'''
print(df.describe())
print(type(df.describe())) '''

'''
csvFilename='grades.csv'
df.to_csv(csvFilename) '''
'''
excelFilename='grades.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data') '''

'''
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary") '''
'''
mean = df.describe().loc['mean','grade']
print(mean) '''

mean = df['grade'].mean()
print(mean)