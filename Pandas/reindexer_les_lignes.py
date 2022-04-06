#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[2]:


new_titanic_survival = titanic_survival.sort_values("age", inplace=False, ascending=False)
new_titanic_survival


# In[3]:


# DataFrame.reset_index(drop=True)


# In[4]:


new_titanic_survival.reset_index()


# ### Réindexer le dataframe new_titanic_survival pour que la première ligne commence à 0 et supprimer l'ancien indexage
# ### Assigner le résultat à la variable titanic_reindexed
# ### Afficher les 5 premières lignes et 3 premières colonnes de titanic_reindexed

# In[6]:


titanic_reindexed = new_titanic_survival.reset_index(drop=True)
titanic_reindexed.iloc[0:5,0:3]
print(titanic_reindexed)


# In[ ]:




