import numpy as np
vector = np.array([10, 20, 30, 35])

print(vector[0])

list_of_lists = [[1, 2, 3], [3, 5, 8]]

print(list_of_lists[0][1])

matrix = np.array([[1, 2, 3], [5, 6, 8], [6,59, 45]])

print(matrix[0, 1])

##Assigner le nombre de litres de vin bu par un Ivoirien en 1985 à la variable Ivoire 1985. Cela correspond à la donnée de la 3e ligne

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

ivoirien_1985 = world_alcohol[2, 4]

print(ivoirien_1985)

##Assigner le nom du pays de la 2e ligne à la variable second_country
second_country = world_alcohol[1, 2]

print(second_country)