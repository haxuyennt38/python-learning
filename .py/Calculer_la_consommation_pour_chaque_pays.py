#!/usr/bin/env python
# coding: utf-8

# ### Créer un dictionnaire vide qui va contenir tous les pays et leurs consommations d'alcohol associées, on le nommera totals    

# In[1]:


totals = {}


# In[2]:


import numpy as np


# In[3]:


world_alcohol =  np.genfromtxt('world_alcohol.csv', delimiter = ',', dtype = 'U75', skip_header = 1)


# ### Sélectionner ensuite les lignes de world_alcohol correspondant à l'année donné, disons 1989. Assigner le résultat à la variable year

# In[4]:


is_year = (world_alcohol[:, 0] == '1989')
year = world_alcohol[is_year, :]
print(year)


# ### Sélectionner dans une liste qu'on nommera countries tous les pays

# In[5]:


countries = world_alcohol[:, 2]
print(countries)


# ### Parcourir tous les pays de la liste à l'aide d'une boucle

# In[6]:


for country in countries :
    is_country = year [:, 2] == country
    country_consumption = year[is_country, :]
    colonne = country_consumption[:, 4]
    empty_colonne = colonne == ''
    colonne[empty_colonne] ='0'
    colonne = colonne.astype(float)
    totals[country] = colonne.sum()
    
    
print(totals)


# ## Trouver le pays qui consomme le plus d'acool

# ### Créer une variable highest_value qui gardera en mémoire la plus grande valeur du dictionnaire totals. On la fixe à 0 pour commencer

# In[7]:


highest_value = 0


# ### Créer une variable similaire qu'on nommera highest_key qui gardera en mémoire le nom du pays associé à la plus grande valeur. On la fixe à la valeur None

# In[8]:


highest_key = None


# ### Parcourir chaque pays du dictionnaire totals

# In[9]:


for country in totals :
    consumption = totals[country]
    if highest_value < consumption :
        highest_value = consumption
        highest_key = country
print(highest_key)

