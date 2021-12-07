import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter =',', dtype = 'U75', skip_header = 1)
#Je ne dois pas utiliser skip_header, sinon quand on utilise le skip_header pour suprrimer la première ligne

print(world_alcohol)