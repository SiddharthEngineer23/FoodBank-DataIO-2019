import pandas as pd
# import folium
import math
import os

os.getcwd()

familyData = pd.read_csv("pt_families.csv", low_memory=False)

x_coords = []
y_coords = []

x = 0
y = 0

for row in range(5):
    latitude = familyData['current_latitude_3_500m'][row]
    longitude = familyData['current_longitude_3_500m'][row]
    
    x_coords.append(latitude)
    y_coords.append(longitude)

    latDist = (latitude - y) ** 2
    lonDist = (longitude - x) ** 2
    distance = math.sqrt(latDist + lonDist)
    distanceD = x * (longitude - x) * (-distance)
    
    sum = sum + distanceD