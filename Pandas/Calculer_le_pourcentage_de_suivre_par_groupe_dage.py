#!/usr/bin/env python
# coding: utf-8

# ### Ajouter la colonne "age_labels" au dataframe titanic_survival contenant la variable age_labels qu'on a créé dans la vidéo précédente.
# ### Créer une table pivot qui calcule la moyen de chance de suivre (colonne "survived") pour chaque groupe d'âge (colonne "age_labels) du dataframe titanic_survival.
# ### Assigner l'objet Series résultant à la variable age_group_survival.
# ### Afficher le résultat.

# In[1]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[2]:


def is_age(row) :
    age = row["age"]
    
    if pd.isnull("age") :
        return "Unknown"
    elif age < 18 :
        return "miror"
    else :
        return "adult"


# In[3]:


age_labels = titanic_survival.apply(is_age, axis = 1)
age_labels


# In[5]:


titanic_survival["age_labels"] = age_labels
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="survived")
print(age_group_survival)


# In[ ]:




