# read a file with Pandas

import pandas as pd

food_info = pd.read_csv("food_info.csv")

print(food_info)

#Use the type() and print() functions to display the type of food_info and confirm that it is a dataframe object

print(type(food_info))

#Exploration of the DataFrame ()

print(food_info.head(2)) #2 première lignes

#Columns

print(food_info.columns)

#dataframe size

dimensions = food_info.shape
print(dimensions)

# Nombre de lignes
num_rows = dimensions[0]
print(num_rows)

# Nombre de colonnes
num_columns = dimensions[1]
print(num_columns)

# Objet serie représentant la ligne d'index 0 ou de position 1
print(food_info.loc[0])

# dataframe.dtypes
print(food_info.dtypes)

#Sélectionner une colonne plutôt qu'une ligne
# Objet Series représentent la colonne "NDB_No"
ndb_col = food_info["NDB_No"]

# 2e méthode en faisant intervenir une variable pour le nom de la colonne
col_name = "NDB_No"
ndb_col = food_info[col_name]

print(ndb_col)

#Assigner la colonne "Protein_(g)" à la variable protein
protein = food_info["Protein_(g)"]

print(protein)

#Cas pratique

col_names = food_info.columns.tolist()

gram_columns = []

for c in col_names :
    if c.endswith("(g)") :
        gram_columns.append(c) #ajouter un dernier élément d'une liste
gram_df = food_info[gram_columns]  

gram_df.head(3)

print(gram_df)