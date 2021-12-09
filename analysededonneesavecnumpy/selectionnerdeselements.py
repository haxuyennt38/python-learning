import numpy as np

vector = np.array([5, 10, 15, 20])

equal_to_ten = (vector == 10)

print(vector[equal_to_ten])

matrix = np.array([[5, 10, 15], [20, 25, 30], [30, 35, 40]])

second_column_25 = (matrix[:, 1]) == 25

print(matrix[second_column_25, :])


#Comparer la 3e colonne de world_alcohol à la chaine de caractères "Algeria". #Sélectionner seulement les lignes de world_alcohol pour lesquelles country_is_algeria vaut True

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

country_is_ageria = (world_alcohol[:, 2]) == 'Algeria'

print(world_alcohol[country_is_ageria])

#Faire la même travail pour récupérer toutes les lignes correspondantes à l'année "1984"

years_1984 = (world_alcohol[:, 0]) == '1984'

print(world_alcohol[years_1984])

#years_1984 = world_alcohol[world_alcohol[:, 0] == '1984']
#print(years_1984)



