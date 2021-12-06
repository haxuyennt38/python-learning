cities = ['Paris' , 'Madrid' , 'Rome']

for city in cities :
    print(city)



fruits = ['Citron' , 'Banane', 'Pomme', 'Banane', 'Pomme', 'Banane', 'Pomme']

fruits_counts = {}

for index in fruits :
    if index in fruits_counts :
        fruits_counts[index] += 1
    else:
        fruits_counts[index] = 1
print(fruits_counts)