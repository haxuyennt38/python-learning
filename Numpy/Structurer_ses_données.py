#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np


# In[57]:


nom = ["Mcgregor", "Nurma", "Hari"]


# In[58]:


prenom = ["Alice", "Abib", "Badr"]


# In[59]:


niveau = [3, 1, 2]


# In[60]:


moy = [12, 17, 15]


# In[61]:


donnees = np.zeros(3, dtype = {"names" :("nom", "prenom","niveau", "moy"), "formats":("U10", "U10","i4", "f8")})


# In[62]:


print(donnees)


# In[63]:


donnees["nom"] = nom
donnees["prenom"] = prenom
donnees["niveau"] = niveau
donnees["moy"] = moy


# In[64]:


print(donnees)


# In[65]:


donnees["nom"]


# In[66]:


donnees[1]


# In[67]:


donnees[0]["nom"]#afficher le premier étudiant par l'utilisation de l'indexation


# In[68]:


#Sélectionner uniquement les étudiants avec le niveau 1 et 2
donnees[1:]["nom"]


# In[69]:


#L'autre facon
donnees[donnees["niveau" ]< 3]["nom"]


# In[ ]:




