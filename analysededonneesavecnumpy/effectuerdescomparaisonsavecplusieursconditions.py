import numpy as np

vector = np.array([5, 10, 15, 20])

equal_to_ten_and_five = (vector == 10) & (vector == 5)

print(equal_to_ten_and_five)

equal_to_ten_or_five = (vector == 10) | (vector == 5)

print(equal_to_ten_or_five)

##Sélectionner les lignes dont le pays est 'Algeria' et l'année "1986"

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

is_algeria_and_1986 = (world_alcohol[:, 2] == 'Algeria') & (world_alcohol[:, 0] == '1986')

print(is_algeria_and_1986)

#Utiliser is_algeria_and_1986 pour sélectionner les lignes correspondantes dans le tableau world_alcohol

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

print(rows_with_algeria_and_1986)