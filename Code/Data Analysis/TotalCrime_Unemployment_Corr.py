import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#read in crime data
crime_df= pd.read_csv('crime_updates.csv')
#read in unemployment data
unemployment_df = pd.read_csv('Unemployment_updates.csv')
print(unemployment_df)

#read unemployment rates into list
unemploy_dict = unemployment_df.to_dict('records')
unemploy = []
for row in unemploy_dict:
    unemploy.append(row['unemployment rate'])

#get count of total crime grouped by month
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
#read crime rate and unemployment into df
corr_df = pd.DataFrame()
corr_df['crime'] = crime
corr_df['unemployment'] = unemploy

#print correlation of total crime and unemployment 
print(corr_df.corr())

x = corr_df['crime']
y = corr_df['unemployment']

plt.scatter(x, y)
plt.xlabel("Monthly Crime Rate per 1000 people")
plt.ylabel("Monthly Unemployment Rate")
plt.title('Monthly Crime Rate vs Monthly Unemployment Rate')

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b, color='red')

plt.savefig('Monthly Crime Rate vs Monthly Unemployment Rate')
plt.clf()

