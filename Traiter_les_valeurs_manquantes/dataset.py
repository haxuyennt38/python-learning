import pandas as pd

titanic_survival = pd.read_csv("titanic_survival.csv")

print(titanic_survival.head())

#Trouver les valeurs manquantes : pandas.isnull()

sex  = titanic_survival["sex"]

sex_is_null = pd.isnull(sex)

print(sex_is_null)

sex_null = sex[sex_is_null]

print(sex_null)


#Compter le nombre de valeurs dans la colonne "age" possédant des valeurs manquantes
age = titanic_survival["age"]

print(age.loc[10:25])

age_is_null = pd.isnull(age) #créer une serie de valeurs True et False

print(age_is_null)

age_null = age[age_is_null] #sélectionner seulement les éléments de la colonne "age" qui sont nuls

print(age_null)

age_null_count = len(age_null)

print(age_null_count)






