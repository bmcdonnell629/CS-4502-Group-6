import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates

#read in crime data
crime_df= pd.read_csv('crime_updates.csv')

crime = crime_df.groupby(['Date'])['Primary Type'].count().tolist()
#divide total crime per month by population / 1000 to crime rate per 1000 people
for i in range(len(crime)):
    if i < 12:
        crime[i] = (crime[i]/2812.0)
    elif i < 24:
        crime[i] = (crime[i]/2817.0)
    elif i < 36:
        crime[i] = (crime[i]/2835.0)
    elif i < 48:
        crime[i] = (crime[i]/2855.0)
    elif i < 60:
        crime[i] = (crime[i]/2697.0)
    elif i < 72:
        crime[i] = (crime[i]/2708.0)
    elif i < 84:
        crime[i] = (crime[i]/2719.0)
    elif i < 96:
        crime[i] = (crime[i]/2726.0)
    elif i < 108:
        crime[i] = (crime[i]/2727.0)
    elif i < 120:
        crime[i] = (crime[i]/2724.0)
    elif i < 132:
        crime[i] = (crime[i]/2716.0)
    elif i < 144:
        crime[i] = (crime[i]/2710.0)
    elif i < 156:
        crime[i] = (crime[i]/2701.0)
    elif i < 168:
        crime[i] = (crime[i]/2691.0)
crime_df['Date'] = pd.to_datetime(crime_df['Date'], format='%Y%m').dt.strftime('%Y%m')
#crime_df.sort_values(by=['Date'])
#print(crime_df['Date'].sort_values('Date'))

#PLot monthly overall crime rate versus times
dateList = crime_df.groupby(['Date'])['Date'].apply(list)

crime_df = crime_df[::-1]
date = crime_df['Date'].unique()
x = crime_df['Date'].unique()
y = crime

fig = plt.figure()
ax = fig.add_subplot()  
plt.plot( x, y )

ax.xaxis.set_major_locator(mdates.MonthLocator())   #to get a tick every 15 minutes
#plt.plot(x, y)
plt.xlabel("Years")
plt.ylabel("Monthly Crime Rate")
plt.title('Monthly Overall Crime Rate 2006 - 2019 ')

plt.savefig('Monthly Crime Rate')
plt.clf()