#!/usr/bin/env python
# coding: utf-8

# ## Introduction au dataset
# ### Lire all_ages.csv dans un DataFrame et l'assigner à la variable all_ages
# ### Lire recent_grads.csv dans un DataFrame et l'assigner à la variable recent_grads
# ### Afficher les 5 premières lignes de all_ages et recent_grads

# In[2]:


import pandas as pd

all_ages = pd.read_csv("all_ages.csv")
recent_grads = pd.read_csv("recent_grads.csv")


# In[3]:


all_ages.head()


# In[4]:


recent_grads.head()


# ## Nombre d'étudiants pas catégorie de Major
# ### Retourner les valeurs uniques de Major_category
# ### Utiliser la méthode Series.unique() pour retourner les valeurs uniques d'une Serie

# In[7]:


all_ages["Major_category"].unique()


# In[8]:


recent_grads["Major_category"].unique()


# ### Pour chque valeur unique (utilisation d'une boucle for?)
# ### Retourner toutes les lignes où Major_category vaut cette valeur unique
# ### Calculer le nombre total d'étudiants représentant cette catégorie de major (colonne Total à sommer)
# ### Vous garderez en mémoire ce résultat sous le forme d'un dictionnaire contenant une Major_category en clé et le nombre d'étudiants en valeur

# In[9]:


all_ages["Total"].sum()


# In[10]:


recent_grads["Total"].sum()


# ## Missions :
# ### Créer une fonction dans laquelle vous utilisez la colonne Total pour calculer le nombre d'étudiants pour chaque catégorie de Major_category dans chaque dataset
# ### - Stocker le résultat dans 2 dictionnaires distincts
# ### - Pour le dataset all_ages, stocker le résultat dans un dictionnaire qu'on nommera aa_cat_counts
# ### - Pour le dataset recent_grads, stocker le résultat dans un dictionnaire qu'on nommera rg_cat_counts
# ### Autre méthode : Utiliser un pivot de table
# ### Afficher les 2 dictionnaires

# In[11]:


def calculate_major_cat_totals(df):
    cats = df["Major_category"].unique()
    counts_dictionnary = dict()
    
    for c in cats :
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum()
        counts_dictionnary[c] = total
    return counts_dictionnary


# In[12]:


aa_cat_counts =  dict()
aa_cat_counts = calculate_major_cat_totals(all_ages)
print(aa_cat_counts)


# In[13]:


rg_cat_counts = dict()
rg_cat_counts =  calculate_major_cat_totals(recent_grads)
print(rg_cat_counts)


# In[14]:


import numpy as np
aa_cat_counts = dict(all_ages.pivot_table(index = "Major_category", values = "Total", aggfunc=np.sum))
print(aa_cat_counts)


# In[15]:


rg_cat_counts = dict(all_ages.pivot_table(index = "Major_category", values = "Total", aggfunc=np.sum))
print(rg_cat_counts)


# ## Taux de jobs à faible salaire
# ### Utiliser les colonnes "Low_wage_jobs" et "Total" pour calculer la proposition de jeunes diplômés qui ont du trouver des jobs à faible salaire (recent_grads)
# ### - Souvenez-vous que vous pouvez utiliser la méthode Series.sum() pour retourner la somme des valeurs d'une colonne
# ### Stocker le résultat dans la variable low_wage_proposition et l'afficher

# In[18]:


low_wage_jobs_total = recent_grads["Low_wage_jobs"].sum()
print(low_wage_jobs_total)
total = recent_grads["Total"].sum()
print(total)


# In[19]:


low_wage_proposition = low_wage_jobs_total/total
print(low_wage_proposition)


# ## Comparer des datasets
# ### Utiliser une boucle for pour parcourir toutes les majors
# ### - Pour chaque Major et chaque DataFrame, filtrer seulement les lignes du DataFrame correspondant à cette major
# ### - Comparer les valeurs pour la colonne "Unemployment_rate" pour voir lequel des 2 DataFrames possèdent la valeur la plus basse
# ### - Incrémenter (cad ajouter 1) à la variable rg_lower_count si la valeur pour Unemployment_rate est plus petite dans le dataframe recent_grads que dans le dataframe all_ages
# ### Afficher le résultat rg_lower_count

# In[20]:


# Liste des majors communes à nos 2 DataFrames
majors = recent_grads["Major"].unique()


# In[25]:


rg_lower_count = 0

for m in majors :
    recent_grads_row =  recent_grads[recent_grads["Major"] == m]
    all_ages_row = all_ages[all_ages["Major"] == m]
    
    rg_unemp_rate = recent_grads_row["Unemployment_rate"].values
    aa_unemp_rate = all_ages_row["Unemployment_rate"].values
    
    if rg_unemp_rate < aa_unemp_rate :
        rg_lower_count += 1
        
print(rg_lower_count)


# In[ ]:




