#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ser = pd.Series([1,3,5,7,9], index = ["a", "b", "c", "d", "e"])
print(ser)


# ### Sélectionner l'élément

# In[3]:


ser["c"]


# ### Vérifier la présence d'un élément dans la série

# In[4]:


"b" in ser


# ### Renvoyer quant à elle la liste des clés   utilisées dans le dictionnaire

# In[5]:


ser.keys()


# In[6]:


list(ser.items())


# In[7]:


ser["e"] = 11


# In[8]:


print(ser)


# In[9]:


ser = pd.Series(["a", "b", "c", "d", "e"], index = [1, 3, 5, 7, 9])


# In[12]:


pib_dict = {"État_Unis" : 18624.48, "Japon":4936.21, "Chine":11218.28, "Allemagne":3477.8, "Royaume_Uni":2647.9}
pib = pd.Series(pib_dict)
pibpop_dict = {"État_Unis" : 57638, "Japon":38972, "Chine":8117, "Allemagne":42232, "Royaume_Uni":40412}
pibpop = pd.Series(pibpop_dict)
pib_pop = pd.DataFrame({"pib/habitant":pibpop, "pib":pib})
print(pib_pop)


# In[13]:


pib_pop["pib"]


# In[14]:


pib_pop["population"] = (pib_pop["pib"]*100000000)/pib_pop["pib/habitant"]


# In[15]:


print(pib_pop)


# In[16]:


pib_pop.values


# In[17]:


pib_pop.T


# In[18]:


pib_pop.T.iloc[:2, :3]


# In[19]:


pib_pop.T.loc[: "pib/habitant", : "Chine"]


# In[20]:


pib_pop[pib_pop["population"] > 100000000]


# In[ ]:




