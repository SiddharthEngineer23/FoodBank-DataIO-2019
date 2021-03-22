import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
# import folium
import os

os.getcwd()

familyData = pd.read_csv("pt_families.csv", low_memory=False)
familyData = familyData.sample(frac=0.2, replace=True, random_state=1)
pantryLocations = pd.read_csv("locations_fixed_20191019.csv")

x_family = familyData['current_latitude_3_500m']
y_family = familyData['current_longitude_3_500m']
family = np.vstack((x_family, y_family)).T
    
x_pantry = pantryLocations['latitude'].to_list()
y_pantry = pantryLocations['longitude'].to_list()
pantry = np.vstack((x_pantry, y_pantry)).T
    
wcss = []

x = 1
y = 750

for i in range(x, y):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, random_state=0)
    kmeans.fit(family)
    wcss.append(kmeans.inertia_)
plt.plot(range(x, y), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('ERROR')
plt.show()

kmeans = KMeans(n_clusters=687, init='k-means++', max_iter=300, random_state=0)
pred_y = kmeans.fit_predict(family)
plt.scatter(x_family, y_family)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()