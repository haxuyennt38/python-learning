#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")


# In[4]:


# Dataframe.pivot_table()


# In[9]:


import numpy
passenger_class_fares = titanic_survival.pivot_table(index = "pclass", values = "fare", aggfunc = numpy.mean) 
#ou passenger_class_fares = titanic_survival.pivot_table(index = "pclass", values = "fare")
print(passenger_class_fares)


# ### Utiliser la méthode dataFrame.pivot_table() pour calculer la moyenne de l'âge pour chauqe classe de passager ("pclass").
# Assigner le résultat à la variable passenger_age.
# Afficher passenger_age

# In[10]:


passenger_age = titanic_survival.pivot_table(index = "pclass", values = "age")


# In[11]:


print(passenger_age)


# ### Faire de même avec la colonne survived pour chaque classe de passager

# In[12]:


passenger_survived = titanic_survival.pivot_table(index = "pclass", values = "survived")


# In[13]:


print(passenger_survived)


# ## Tables Pivot Niveau 2

# ### Faire un pivot de table qui calcule le total d'agent encaissé ("fare") et le nombre de survived ("survived") pour chaque port d'embarcation ("embarked"). Il faudra utiliser la fonction numpy.sum

# In[14]:


embarked_fare = titanic_survival.pivot_table(index = "embarked", values = "fare", aggfunc = numpy.sum)
print(embarked_fare)


# In[15]:


embarked_survived = titanic_survival.pivot_table(index = "embarked", values = "survived", aggfunc = numpy.sum)
print(embarked_survived)


# Assigner le résultat à la variable port_stats. Afficher le résultat

# In[16]:


port_stats = titanic_survival.pivot_table(index = "embarked", values = ["fare", "survived"], aggfunc = numpy.sum)
print(port_stats)


# In[ ]:




