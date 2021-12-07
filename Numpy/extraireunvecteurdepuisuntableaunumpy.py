import numpy as np
vector = np.array([12, 14, 34, 45])

print(vector[0:3])

matrix = np.array([[23, 45, 56], [34, 55, 68], [67, 89, 40]])

print(matrix)

print(matrix[:, 1])

print(matrix[2, :])

print(matrix[1:2, 1])

##Assigner toute la 3e colonne de world_alcohol à la variable countries

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

print(world_alcohol[:, 2])

##assigner l'ensemble de la 5e colonne de world_alcolhol à la variable alcoholl_consumption

alcohol_comsumption = world_alcohol[:, 4]
print(alcohol_comsumption)