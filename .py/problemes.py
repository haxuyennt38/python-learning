#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


titanic_survival = pd.read_csv("titanic_survival.csv")
mean_age = sum(titanic_survival["age"])/len(titanic_survival["age"])
mean_age


# Utiliser age_is_null pour créer un vecteur qui contient les valeurs de la colonne "age" qui ne sont pas NaN (c'est à dire pour lesquelles age_is_null vaut False)

# In[7]:


age = titanic_survival["age"]


# In[9]:


age_is_null = pd.isnull(age)
print(age_is_null)


# Assigner ce résultat à la variable good_ages

# In[19]:


good_ages = titanic_survival["age"][age_is_null == False]


# In[20]:


print(good_ages)


# Calculer la moyenne de ce nouveau vecteur et assigner le résultat à la variable mean_age

# In[21]:


mean_age = sum(good_ages)/len(good_ages)
print(mean_age)


# ### Calculer une moyenne plus simplement

# In[22]:


# series.mean()


# In[24]:


mean_ages = titanic_survival["age"].mean()


# In[25]:


print(mean_ages)


# Assigner la moyenne de la colonne "fare" à la variable mean_fare

# In[26]:


mean_fare = titanic_survival["fare"].mean()
print(mean_fare)


# In[ ]:




