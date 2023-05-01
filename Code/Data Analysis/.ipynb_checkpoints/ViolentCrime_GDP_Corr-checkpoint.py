import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#read in crime data
crime_df= pd.read_csv('violent_crime_updates.csv')
#read in unemployment data
gdp_df = pd.read_csv('GDP_2006_2019.csv')

#read unemployment rates into list
GDP_dict = gdp_df.to_dict('records')
gdp = []
for row in GDP_dict:
    gdp.append(row['GDP(Billion)'])

#get count of total crime grouped by year
crime = crime_df.groupby(['Year'])['Primary Type'].count().tolist()
for i in range(len(crime)):
    if i == 0:
        crime[i] = (crime[i]/2812.0)
    elif i ==1:
        crime[i] = (crime[i]/2817.0)
    elif i == 2:
        crime[i] = (crime[i]/2835.0)
    elif i == 3:
        crime[i] = (crime[i]/2855.0)
    elif i == 4:
        crime[i] = (crime[i]/2697.0)
    elif i == 5:
        crime[i] = (crime[i]/2708.0)
    elif i == 6:
        crime[i] = (crime[i]/2719.0)
    elif i == 7:
        crime[i] = (crime[i]/2726.0)
    elif i == 8:
        crime[i] = (crime[i]/2727.0)
    elif i == 9:
        crime[i] = (crime[i]/2724.0)
    elif i == 10:
        crime[i] = (crime[i]/2716.0)
    elif i == 11:
        crime[i] = (crime[i]/2710.0)
    elif i == 12:
        crime[i] = (crime[i]/2701.0)
    elif i == 13:
        crime[i] = (crime[i]/2691.0)
#read crime rate and unemployment into df
corr_df = pd.DataFrame()
corr_df['crime'] = crime
corr_df['GDP'] = gdp

#print correlation of violent crime and gdp
print(corr_df.corr())

#plot violent crime rate vs gdp
x = corr_df['crime']
y = corr_df['GDP']

plt.scatter(x, y)
plt.xlabel("Annual Violent Crime Rate per 1000 people")
plt.ylabel("GDP in Billions Adjusted to 2012 dollars")
plt.title('Annual Violent Crime Rate vs GDP')

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b, color='red')

plt.savefig('Annual Violent Crime Rate vs GDP')
plt.clf()
