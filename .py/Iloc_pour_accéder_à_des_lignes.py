#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
print(titanic_survival)


# In[2]:


#DataFrame.loc[]


# In[3]:


new_titanic_survival = titanic_survival.sort_values("age", inplace = False, ascending = False)
#age_décroissance
new_titanic_survival


# In[4]:


new_titanic_survival.loc[0]


# In[5]:


#DataFrame.iloc[]


# In[6]:


new_titanic_survival.iloc[0:5]


# Assigner les 10 premières lignes de new_titanic_survival à la variable first_ten_rows

# In[13]:


first_ten_rows = new_titanic_survival.iloc[0:10]


# In[8]:


print(first_ten_rows)


# Assigner la 5e ligne de new_titanic_survival à la variable row_position_fifth

# In[9]:


row_position_fifth = new_titanic_survival.iloc[4]


# In[10]:


print(row_position_fifth)


# Assigner la ligne dont l'intitulé d'index est 25 pour new_titanic_survival à la variable row_index_25

# In[11]:


row_index_25 = new_titanic_survival.loc[25]


# In[12]:


print(row_index_25)


# In[ ]:




