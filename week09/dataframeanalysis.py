# dataframeanalysis.py
# this program do some data analysis
# Author: Fatima Zeino

import pandas as pd
import re

logFilename ='access.log'

colNames= ('ip',
'dash1',
'userId',
'time',
'url',
'status code',
'size of response',
'referer',
'user agent',
'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

#df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
#df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#print(df)

newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#print(newdf) 

downloadSamples = df['size of response'].resample(rule='30Min').mean()
#print(downloadSamples)

downloadSamples.plot()
plt.show()