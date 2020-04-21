#!/usr/bin/env python
# coding: utf-8

# In[1]:


# masukkan library yang akan kita gunakan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# melakukan pembacaan pada dataset dalam format csv
data = pd.read_csv('tugas3.csv')


# In[2]:


data.info()


# In[4]:


#print 10 data pertama dalam tabel
data.head(10)


# In[5]:


#dimensi data
data.shape


# In[6]:


#deskripsi data
data.describe()


# In[7]:


data.corr()


# In[9]:


correlations = data.corr(method = "kendall")
correlations


# In[10]:


# correlation map
# higher correlations are brighter
f,ax = plt.subplots(figsize=(20,20))
sns.heatmap(correlations, annot=True, linewidths=.5, fmt='.3f', ax=ax)
plt.show


# In[ ]:




