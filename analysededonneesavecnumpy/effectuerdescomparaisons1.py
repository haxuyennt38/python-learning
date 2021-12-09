import numpy as np

vector = np.array([5, 10, 15, 20])

equal_to_ten = (vector == 10)

print(equal_to_ten)


matrix = np.array([[10, 25, 30], [45, 50, 55], [60, 65, 70]])

equal_to_25 = (matrix[:, 1]) == 25

print(equal_to_25)


##Lire le dataset world_alcohol.csv dans la variable world_alcohol

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

#Extraire le 3e colonne de world_alcohol et comparer la au pays "Canada". Assigner le résultat à la variable countries_canada
countries_canada = world_alcohol[:, 2]

print(countries_canada == 'Canada')

#Xtraire la première colonne de world_alcohol et comparer la chaine de caratères "1984". Assigner les résultat à la variable years_1984

years_1984 = world_alcohol[:, 0]

print(years_1984 == '1984')