import numpy as np

vector = np.array(['1', '2', '3'])

vector = vector.astype(float)

print(vector)

#Extraire la 5e colonne de world_alcohol et assigner le résultat à la variable alcohol_consumption

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header = 1)

alcohol_consumption = world_alcohol[:, 4]


#Utiliser la méthode astype() pour convertir alcohol_consumption en décimal (float)

alcohol_consumption = alcohol_consumption.astype(float)

print(alcohol_consumption)