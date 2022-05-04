#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


rand = np.random.RandomState(20)
x = rand.randint(10, size = 20)
print(x)


# In[6]:


#Accéder à deux éléments différents
[x[0], x[12]]


# In[7]:


#L'indexation fancy : procéder consiste à passer une liste unique ou un tableau d'indices
ind = [0, 12]
x[ind]


# In[8]:


#La combinaison d'indices
y = np.arange(9).reshape((3,3))
print(y)


# In[9]:


y[1, [1, 0, 2]]


# In[10]:


y[1: ,[1, 0, 2]]


# In[ ]:




