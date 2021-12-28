#!/usr/bin/env python
# coding: utf-8

# ## Créer un dictionnaire vide qu'on nommera fares_by_class

# In[2]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[10]:


fares_by_class ={}
fares_by_class


# ## Créer la liste passenger_classes qui contient les éléments [1, 2, 3]

# In[11]:


passenger_classes = [1, 2, 3]
passenger_classes


# ## Utiliser une boucle for pour parcourir la liste passenger_classes

# ### Sélectionner juste les lignes de titanic_survival pour lesquelles la colonnes pclass est égale à la variable temporaire (l'intérieur) de la boucle for, c'est à dire correspondant au numéro de classe (1, 2 ou 3)
# ### Utiliser la méthode Series.mean() pour calculer la moyenne de ce sous-ensemble
# ### Ajouter cette moyenne calculée de la classe au dictionnaire fares_by_class avec comme clé le numéro de la classe (et donc comme valeur la moyenne du prix du billet d'embarquement

# In[13]:


for this_class in passenger_classes :
    pclass_rows = titanic_survival[titanic_survival["pclass"] == this_class]
    pclass_fares = pclass_rows["fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print(fares_by_class)


# In[ ]:




