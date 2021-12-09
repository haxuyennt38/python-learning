import numpy as np

vector = np.array([5, 10, 15, 20])

equal_to_ten_or_five = (vector == 10) | (vector == 5)

print(equal_to_ten_or_five)

vector[equal_to_ten_or_five] = 25

print(vector[equal_to_ten_or_five])

print(vector)

matrix = np.array([[5, 10, 15], [10, 25, 40], [45, 50, 55]])

second_row_25 = (matrix[:, 1]) == 25

print(second_row_25)

matrix[second_row_25] = 10

print(matrix)


#Créer un tableau numpy world_alcohol_2 égal world_alcohol pour le dupliquer sous un autre nom

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

world_alcohol_2 = world_alcohol.copy()

world_alcohol_2[:, 0][world_alcohol_2[:, 0] == '1986'] = '2018'

world_alcohol_2[:, 3][world_alcohol_2[:, 3] == 'Wine'] = 'Beer'

print(world_alcohol_2)

