#!/usr/bin/env python
# coding: utf-8

# In[15]:


# DataFrame.apply(function, axis = 1)


# In[16]:


import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
titanic_survival


# In[17]:


def is_minor(row) :
    if row["age"] < 18 :
        return True
    else :
        return False


# In[18]:


minors = titanic_survival.apply(is_minor, axis = 1)
minors


# In[19]:


def which_class(row) :
    pclass = row["pclass"]
    
    if pd.isnull(pclass) :
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2 :
        return "Second Class"
    else :
        return "Third Class"


# In[20]:


classes = titanic_survival.apply(which_class, axis = 1)
classes


# ### Créer une fonction qui retourne la chaine de caractère "miror" pour quelqu'un de moins de 18 ans, "adult" si son age est supérieur ou égal à 18 et "unknown" si la valeur est manquante.
# ### Utiliser cette focntion avec la méthose apply() pour trouver l'intitulé correct pour chaque apssager du dataframe titanic_survival.
# ### Assigner le résultat à la variable age_labels.
# ### Afficher le résultat.

# In[23]:


def is_age(row) :
    age = row["age"]
    
    if pd.isnull(age) :
        return "Unknown"
    elif age < 18 :
        return "miror"
    else :
        return "adult"


# In[24]:


age_labels = titanic_survival.apply(is_age, axis = 1)
print(age_labels)


# In[ ]:




