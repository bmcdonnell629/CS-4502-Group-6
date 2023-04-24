import pandas as pd

#read unemployment data into df
df= pd.read_csv('Unemployment_2001_2022.csv')

#convert df to dict
df_dict = df.to_dict('records')
#convert year month format into yyyymm format
for row in df_dict:
    if row['Period'] == 'Jan':
        row['Period'] = format(1, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Feb':
        row['Period'] = format(2, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Mar':
        row['Period'] = format(3, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Apr':
        row['Period'] = format(4, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'May':
        row['Period'] = format(5, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Jun':
        row['Period'] = format(6, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Jul':
        row['Period'] = format(7, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Aug':
        row['Period'] = format(8, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Sep':
        row['Period'] = format(9, '02d')
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Oct':
        row['Period'] = 10
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Nov':
        row['Period'] = 11
        row['Year'] = int(str(row['Year']) + str(row['Period']))
    elif row['Period'] == 'Dec':
        row['Period'] = 12
        row['Year'] = int(str(row['Year']) + str(row['Period']))
#convert dict to df
new_df = pd.DataFrame.from_dict(df_dict)

#write df to csv
new_df.to_csv('Unemployment_updates.csv', sep=',', encoding='utf-8', index=False)

