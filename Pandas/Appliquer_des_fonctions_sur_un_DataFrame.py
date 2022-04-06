#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DataFrame.apply()


# In[2]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[3]:


# Soit une fonction qui retourne le 100e élément

def row_100(column) :
    # Extraire le 100e élément d'une colonne
    item = column.iloc[99]
    return item


# In[4]:


# retourne le 100e élément de chaque colonne
row_100_var = titanic_survival.apply(row_100)
row_100_var


# ### Ecrire une fonction qui compte le nombre d'éléments manquants d'un objet Series
# ### Utiliser la méthode DataFrame.apply() pour appliquer votre fonction sur titanic_survival
# ### Assigner le résultat à la variable column_null_count
# ### Afficher le résultat

# In[8]:


def null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null] #manquant
    return len(null)


# In[9]:


column_null_count = titanic_survival.apply(null_count)
print(column_null_count)


# In[ ]:




