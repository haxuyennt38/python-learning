import numpy as np

vector = np.array([5, 10, 15, 20])

print(vector.sum())

print(vector.mean())

print(vector.max())

matrix = np.array([[5, 10, 15, 20], [20, 25, 30, 35], [20, 45, 50, 55]])

print(matrix.sum(axis=1))

print(matrix.sum(axis=0))

#Utiliser la méthode sum() pour calculer la somme des valeurs de alcohol_consumption. Assigner le résultat à la variable total_alcohol

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header = 1)

alcohol_comsumption = world_alcohol[:, 4]

alcohol_comsumption = alcohol_comsumption.astype(float)

def new_func(alcohol_comsumption):
    total_alcohol = alcohol_comsumption.sum()
    return total_alcohol

total_alcohol = new_func(alcohol_comsumption)

print(total_alcohol)

#tiliser la méthode mean() pour calculer la moyenne des valeurs de alcohol_consumption. Assigner le résultat à la variable average_alcohol

average_alcohol = alcohol_comsumption.mean()

print(average_alcohol)