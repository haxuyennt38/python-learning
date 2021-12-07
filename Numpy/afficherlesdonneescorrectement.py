import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter =',', dtype = 'U75', skip_header = 1)
#Je ne dois pas utiliser skip_header 

print(world_alcohol)