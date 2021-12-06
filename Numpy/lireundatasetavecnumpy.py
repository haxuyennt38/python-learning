##Lire un dataset avec Numpy

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',')

print(type(world_alcohol))