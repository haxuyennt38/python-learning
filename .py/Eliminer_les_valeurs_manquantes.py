#!/usr/bin/env python
# coding: utf-8

# In[2]:


# DataFrame.dropna(axis = 0 ou axis = "index") - axis = 1


# In[3]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")


# In[4]:


drop_na_rows = titanic_survival.dropna(axis = 0)
drop_na_rows


# In[5]:


drop_na_columns = titanic_survival.dropna(axis = 1)
drop_na_columns


# In[6]:


# dropna(axis = ..., subset = ["name"]) 


# In[7]:


titanic_survival.dropna(axis = 0, subset = ["name"])


# ### Supprimer toutes les linges de titanic_survival pour lesquelles les colonnes "age" ou "sex" ont des valeurs manquantes et assigner le résultat à la variables new_titanic_survival
# ### Comparer le nombre de ligne qu'il reste avec l'attribut shape

# In[9]:


new_titanic_survival = titanic_survival.dropna(axis = 0, subset =["age", "sex"])
new_titanic_survival


# In[10]:


print(new_titanic_survival.shape)


# In[ ]:




