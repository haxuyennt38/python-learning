totals = {}
import numpy as np
world_alcohol =  np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)
is_year = (world_alcohol[:, 0] == '1989')
year = world_alcohol[is_year, :]
print(year)
countries = world_alcohol[:, 2]
print(countries)
for country in countries :
    is_country = year [:, 2] == country
    country_consumption = year[is_country, :]
    colonne = country_consumption[:, 4]
    empty_colonne = colonne == ''
    colonne[empty_colonne] ='0'
    colonne = colonne.astype(float)
    totals[country] = colonne.sum()
    
    
print(totals)