#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pib_dict = {"État_Unis" : 18624.48, "Japon":4936.21, "Chine":11218.28, "Allemagne":3477.8, "Royaume_Uni":2647.9}


# ### Construire une série à partir de ce dictionnaire

# In[4]:


pib = pd.Series(pib_dict)


# In[5]:


print(pib)


# ### Créer une série contenant les PIB par habitant des 5 pays

# In[6]:


pibpop_dict = {"État_Unis" : 57638, "Japon":38972, "Chine":8117, "Allemagne":42232, "Royaume_Uni":40412}
pibpop = pd.Series(pibpop_dict)


# In[7]:


print(pibpop)


# ### Créer le premier DataFrame à partir de ces 2 séries

# In[9]:


pib_pop = pd.DataFrame({"pib/habitant":pibpop, "pib":pib})
print(pib_pop)


# In[10]:


pib_pop.columns


# In[11]:


pib_pop.index


# In[19]:


pd.DataFrame([{"alex": 12, "ibrahim": 11, "sara":15}, {"alex": 14, "ibrahim": 15}, {"alex": 15, "sara" : 16}], index = ["Francais", "Mathématiques", "Anglais"])


# In[20]:


import numpy as np


# In[21]:


pd.DataFrame(np.random.rand(2,2), columns = ["e1", "e2"], index = ["a", "b"])


# ### Utiliser l'indexation Fancy

# In[22]:


ind = pd.Index(["Francais", 'Mathématiques', "Anglais"])


# In[23]:


ind[2]


# In[24]:


ind[2::]


# In[25]:


print(ind.size, "&", ind.shape, "&", ind.ndim, "&", ind.dtype)


# In[26]:


ind1 = pd.Index(["Francais", "Mathématiques", "Anglais"])
ind2 = pd.Index(["Francais", "Sciences"])


# ### Utiliser l'opération de l'intersection

# In[33]:


ind1.intersection(ind2)


# ### Utiliser l'opération de l'union

# In[35]:


ind1.union(ind2)


# In[39]:


ind1.symmetric_difference(ind2)


# In[ ]:




