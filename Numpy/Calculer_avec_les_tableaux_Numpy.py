#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np


# In[21]:


def calcul_inverse(valeur):
    resultat = np.empty(len(valeur))
    for i in range(len(valeur)):
        resultat[i] = 1.0 / valeur[i]
    return resultat


# In[22]:


valeur = np.arange(2, 12, 2)


# In[23]:


calcul_inverse(valeur)


# In[25]:


valeur1 = np.arange(2, 1000000, 2)
#timeit calcul_inverse(valeur1)


# In[27]:


ar = np.arange(2, 12)


# In[31]:


print("ar = ", ar)
print("ar + 1 =", ar + 1, np.add(ar, 1))
print("ar - 1 =", ar + 1, np.subtract(ar, 1))
print("-ar =", -ar,"=", np.negative(ar))
print("ar * 2 =", ar * 2, np.multiply(ar, 2))
print("ar / 2 =", ar / 2, np.divide(ar, 2))
print("ar ** 2 =", ar ** 2, np.power(ar, 2))
print("ar % 2 =", ar % 2, "=", np.mod(ar, 2))


# In[32]:


x = np.linspace(0, 10, 100)


# In[33]:


sinx = np.sin(x)
cosx = np.cos(x)


# In[35]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[36]:


plt.plot(x, sinx)
plt.plot(x, cosx, "x")


# In[37]:


np.add.reduce(ar)


# In[38]:


np.multiply.reduce(ar)


# In[39]:


np.add.outer(ar, ar)


# In[ ]:




