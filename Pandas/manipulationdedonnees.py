import pandas as pd
food_info = pd.read_csv('food_info.csv')
print(food_info)

# Utiliser l'attribut Dataframe.columns suivi de la méthode Index.tolist() pour retourner une liste concernant tous les noms de colonne de food_info

col_names = food_info.columns.tolist()

print(col_names)

#Afficher 3 premières éléments de food_info

print(food_info.head(3))

#Transformer une colonne

div_1000 = food_info["Iron_(mg)"]/1000

print(div_1000)

iron = food_info["Iron_(mg)"]

print(iron)

#Diviser la colonne "Sodium_(mg)" par 1000 pour convertir cette colonne en grammes et assigner le résultats à variable sodium_grams
sodium_grams = food_info['Sodium_(mg)'] / 1000
print(sodium_grams)


sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000
print(sugar_milligrams)



#water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy)

print(food_info[["Water_(g)", "Energ_Kcal"]][0:5])

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
print(grams_of_protein_per_gram_of_water)


milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]
print(milligrams_of_calcium_and_iron)

protein = food_info["Protein_(g)"] * 2
print(protein)

fat = food_info["Lipid_Tot_(g)"] * (-0.75)
print(fat)


rating = protein + fat
print(rating)

#Normaliser des colonnes

# Valeur max de la colonne "Energ_Kcal"
max_calories = food_info["Energ_Kcal"].max()
print(max_calories)

# Diviser les valeurs de la colonne "Energ_Kcal" par la valeur max de cette même colonne
normalized_calories = food_info["Energ_Kcal"] / max_calories
print(normalized_calories)

max_protein = food_info["Protein_(g)"].max()
print(max_protein)
normalized_protein = food_info["Protein_(g)"] / max_protein
print(normalized_protein)

max_fat = food_info["Lipid_Tot_(g)"].max()
print(max_fat)
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat
print(normalized_fat)


#Créer une nouvelle colonne

iron_grams = food_info["Iron_(mg)"] / 1000
food_info["Iron_(g)"] = iron_grams
print(food_info)

food_info["Normalized_Protein"] = normalized_protein
print(food_info)

food_info["Normalized_Fat"] = normalized_fat
print(food_info)

print(food_info.head(5))

#Utiliser les colonnes Normalized_Protein et Normalized_Fat avec cette formule pour créer une nouvelle colonne qu'on nommera Nom_Nutr_Index

# Score = 2 x Normalized_Protein - 0.75 x Normalized_Fat
score = food_info["Normalized_Protein"] * 2 - food_info["Normalized_Fat"] * 0.75
food_info["Nom_Nutr_Index"] = score
print(food_info)

#Trier un DataFrame

# sort_values()
food_info.sort_values("Sodium_(mg)")

# Trier le dataframe et remplacer l'ancien dataframe
food_info.sort_values("Sodium_(mg)", inplace = True)

food_info.sort_values('Sodium_(mg)', inplace = True, ascending = False)

print(food_info)