#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([7, 1, 5, 2, 3])
a.sort()


# In[4]:


print(a)


# In[5]:


#Utiliser l'indexation Fancy
ind = np.argsort(a) #Retourner les indices du tri
print(ind)


# In[6]:


print(a[ind])


# In[8]:


rand = np.random.RandomState()
Mat = rand.randint(1, 9, (3,4))
print(Mat)


# In[9]:


np.sort(Mat, axis = 0)


# In[13]:


np.sort(np.sort(Mat, axis = 0), axis = 1)


# In[15]:


np.partition(a,3)


# In[16]:


Mat1 = rand.randint(1,20,30).reshape(15,2) #15 points, 2 dimensions
print(Mat1)


# In[17]:


import matplotlib.pyplot as plt


# In[21]:


plt.scatter(Mat1[:, 0], Mat1[:, 1]);


# In[25]:


#Calculer la dictance entre chaque paire de points
Mat_disk = np.sum((Mat1[:,np.newaxis,:] - Mat1[np.newaxis, :, :]) ** 2, axis = -1)
print(Mat_disk)


# In[27]:


nearest = np.argsort(Mat_disk, axis = 1)
print(nearest)


# In[28]:


K = 3
nearest_partition = np.argpartition(Mat_disk, K+1, axis = 1)
print(nearest_partition)


# In[ ]:




