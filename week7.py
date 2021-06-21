#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:08:59 2021

@author: Cait
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

shapefile='/Users/Cait/Desktop/Matplot/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country','country_code', 'geometry']
gdf.head()
gdf.plot()
#print(gdf)
dir1 = "/Users/Cait/Desktop/Matplot/"
data_filename = "Rich.csv"
data1= pd.read_csv(dir1+data_filename,names=['country','number'])
data1.head()
gdf['coords']=gdf['geometry'].apply(lambda x: x.representative_point().coords[:])
gdf['coords']=[coords[0]for coords in gdf['coords']]
ax=gdf.to_crs(epsg=4326).plot()
ax.set_axis_off()
for idx, row in gdf.iterrows():plt.annotate(s=row['country'], xy=row['coords'],horizontalalignment='center')
merged=gdf.merge(data1,left_on='country', right_on='country')
merged.head()
#print(data1)
#print(merged)
merged.plot()
ft='number'
plate=merged.to_crs(epsg=4326)
#print(plate)
ax=plate.plot(column=ft,scheme="fisher_jenks",k=15,cmap="Greens",legend=True,alpha=1,linewidth=1,figsize=(50,100))
ax.set_title("Top 500 Richest People by Country, 2021", fontsize = 30)
ax.set_axis_off()
for idx, row in gdf.iterrows():plt.annotate(s=row['country'], xy=row['coords'], horizontalalignment='center')



