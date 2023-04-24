import pandas as pd

#reda in crime data
df= pd.read_csv('Property_Crimes_2006-2019.csv')

#convert date to yyyymm format
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y%m')

#write data out to new csv
df.to_csv('Property_Crime_updated.csv', sep=',', encoding='utf-8', index=False)