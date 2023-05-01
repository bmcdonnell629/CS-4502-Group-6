import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from sklearn.cluster import KMeans
import descartes
import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd
from shapely.geometry import Point, Polygon
from geopandas import GeoDataFrame
df = pd.read_csv('propertyloc_crime_updates.csv')
print(df)
df = df[df['Latitude'] >= 37]
coords = []
coord_dict = df.to_dict('records')
for row in coord_dict:
    coords.append((row['Latitude'], row['Longitude']))
kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
)
kmeans.fit(coords)
# save results
labels = kmeans.labels_
df['cluster'] = labels
_clusters = df.groupby('cluster')['Primary Type'].count()
print(_clusters)
crs = {'init':'epsg:4326'}

chicago_map = gpd.read_file('geo_export_2d0aa425-f4ec-4923-b93f-39319770a138.shp')
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]

geo_df = gpd.GeoDataFrame(df, #specify our data
                          crs=crs, #specify our coordinate reference system
                          geometry=geometry) #specify the geometry list we created
fig, ax = plt.subplots(figsize=(15,15))
chicago_map.plot(ax=ax, alpha=0.4, color='grey')



geo_df[geo_df['cluster'] == 0].plot(ax=ax, 
                                       markersize=20, 
                                       color='blue', 
                                       marker='o',
                                       label = 'Cluster 1')
geo_df[geo_df['cluster'] == 1].plot(ax=ax, 
                                       markersize=20, 
                                       color='red', 
                                       marker='^',
                                       label = 'Cluster 2')
geo_df[geo_df['cluster'] == 2].plot(ax=ax, 
                                       markersize=20, 
                                       color='yellow', 
                                       marker='+',
                                       label = 'Cluster 3')
plt.legend(prop={'size':15})
plt.title('K-Means Clustering of Property Crimes')
plt.show()
plt.savefig('KMeans_PropertyCrimes')

unemployment_df = pd.read_csv('Unemployment_updates.csv')

#read unemployment rates into list
unemploy_dict = unemployment_df.to_dict('records')
unemploy = []
for row in unemploy_dict:
    unemploy.append(row['unemployment rate'])
crime = df.groupby(['Date', 'cluster'])['Primary Type'].count().tolist()
cluster1 = []
cluster2 = []
cluster3 = []
for i in range(len(crime)):
    if i % 3 == 0:
        cluster1.append(crime[i])
    elif i % 3 == 1:
        cluster2.append(crime[i])
    elif i % 3 == 2:
        cluster3.append(crime[i])


corr_df = pd.DataFrame()
corr_df['cluster'] = cluster1
corr_df['unemployment'] = unemploy

print(corr_df.corr())

corr_df['cluster'] = cluster2

print(corr_df.corr())

corr_df['cluster'] = cluster3

print(corr_df.corr())