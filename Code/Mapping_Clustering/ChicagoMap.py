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

chicago_map = gpd.read_file('geo_export_2d0aa425-f4ec-4923-b93f-39319770a138.shp')

fig, ax = plt.subplots(figsize=(15,15))
chicago_map.plot(ax=ax, alpha=0.4, color='grey')

plt.savefig('Chicago_Map')