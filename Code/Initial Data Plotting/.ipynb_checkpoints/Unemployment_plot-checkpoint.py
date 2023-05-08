import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates

#uread in unemploy data
unemploy_df= pd.read_csv('Unemployment_update_form.csv')
unemploy_df['Year'] = pd.to_datetime(unemploy_df['Year'], format='%Y-%m').dt.strftime('%Y-%m')
df = pd.DataFrame()

#plot line graph of unemployment rate
x = unemploy_df['Year']
y  = unemploy_df['unemployment rate']

fig = plt.figure()
ax = fig.add_subplot()  
plt.plot( x, y )

ax.xaxis.set_major_locator(mdates.MonthLocator())   #to get a tick every 15 minutes
#plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Monthly Unemployment Rate")
plt.title('Monthly Unemployment Rate 2006 - 2019 ')

plt.savefig('Monthly Unemployment Rate')
plt.clf()