import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as mdates

#read in GDP data
df= pd.read_csv('GDP_2006_2019.csv')
df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.strftime('%Y')


#plot gdp versus time
x = df['Year']
y = df['GDP(Billion)']

fig = plt.figure()
ax = fig.add_subplot()  



plt.plot( x, y )
plt.xticks(rotation=45)
#ax.xaxis.set_major_locator(mdates.YearLocator(base=2))#to get a tick every 15 minutes
#plt.plot(x, y)
plt.xlabel("Years")
plt.ylabel("GDP(billions)")
plt.title('Chicago GDP 2006 - 2019')

plt.savefig('Annual Chicago GDP')
plt.clf()