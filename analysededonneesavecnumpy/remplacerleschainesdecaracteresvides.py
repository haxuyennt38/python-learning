import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

#Comparer tous les éléments de la 5e colonne de world_alcohol avec la chaine de caractères vides c'est-à-dire ''. Assigner le résultat à la variable is_value_empty

is_value_empty = (world_alcohol[:, 4] == '')

#Remplacer par la chiane de caractères '0'

world_alcohol[is_value_empty, 4] = '0'

print(world_alcohol)


