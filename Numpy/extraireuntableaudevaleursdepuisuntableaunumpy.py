import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter =',', dtype = 'U75', skip_header = 1)

##Assigner toutes les lignes des 2 premières colonnes de world_alcohol à la variable first_two_columns

first_two_columns = world_alcohol[:,0:2]

print(first_two_columns)

##Assigner les 10 premières lignes de la première colonne de world_alcohol à la variable first_ten_years

first_ten_years = world_alcohol[0:10, 0]

print(first_ten_years)

##Assigner les 10 premières lignes de toutes les colonnes de world_alcohol à la variable first_ten_rows

first_ten_rows = world_alcohol[0:10, :]

print(first_ten_rows)

##Assigner les 20 premières lignes des colonnes d'indice 1 et 2 de world_alcohol à la variable first_twenty_regions

first_twenty_regions = world_alcohol[0:20, 1:3]

print(first_twenty_regions)