import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)

is_canada_1986 = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Canada')

canada_1986 = world_alcohol[is_canada_1986, :]

print(canada_1986)

canada_alcohol = canada_1986[:, 4]

empty_strings = canada_alcohol == ''

canada_alcohol[empty_strings] = '0'

canada_alcohol = canada_alcohol.astype(float)

print(canada_alcohol)

total_canadian_drinking = canada_alcohol.sum()

print(total_canadian_drinking)

