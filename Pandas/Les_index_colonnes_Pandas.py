#!/usr/bin/env python
# coding: utf-8

# ## Les index de colonne

# In[4]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[10]:


new_titanic_survival = titanic_survival.sort_values("age", inplace=False, ascending=False)
new_titanic_survival


# In[15]:


# La méthode .iloc
new_titanic_survival.iloc[0,0] #afficher la première positions


# In[16]:


new_titanic_survival.iloc[:,0:3] #afficher toutes les lignes et trois colonnes


# In[17]:


#La méthoe .loc


# In[19]:


new_titanic_survival.loc[83,"age"] #afficher la position 83 de la colonne "age"


# In[21]:


new_titanic_survival.loc[766,"pclass"]


# ### Assigner la valeur d'intitulé de ligne 1100 pour la colonne "age" de new_titatic_survival à la variable row_index_1100_age

# In[30]:


row_index_1100_age = new_titanic_survival.loc[1100,"age"]
print(row_index_1100_age)


# ### Assigner la valeur d'intitulé de ligne 25 pour la colonne "survived" de new_titanic_survival à la variable row_index_25_survived

# In[28]:


row_index_25_survived = new_titanic_survival.loc[25,"survived"]
print(row_index_25_survived)


# ### Assigner les 5 premières lignes et 3 premières colonnes de new_titanic_survival à la variable five_rows_three_cols

# In[29]:


five_row_three_cols = new_titanic_survival.iloc[0:5,0:3]
print(five_row_three_cols)


# In[ ]:




