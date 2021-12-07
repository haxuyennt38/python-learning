import numpy as np

numbers = np.array([1, 2, 3])

print(numbers.dtype)


##Assigner le type de données de world_alcohol à la variable world_alcohaol_dtype
#Afficher world_alcohol_dtype

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',')

print(world_alcohol.dtype)
