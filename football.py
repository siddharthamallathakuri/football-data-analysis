#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[8]:


fifa = pd.read_csv(r"C:\Users\Acer Nitro\Downloads\archive\players_20.csv")
fifa


# In[9]:


fifa.head()


# In[13]:


for col in fifa.columns:
    print(col)


# In[14]:


fifa.shape


# In[18]:


fifa["nationality"].value_counts()


# In[22]:


fifa["nationality"].value_counts()[0:10]


# In[30]:


fifa["nationality"].value_counts()[0:5].index


# In[35]:


plt.figure(figsize=(8,5))
plt.bar(list(fifa["nationality"].value_counts()[0:5].keys()),list(fifa["nationality"].value_counts()[0:5]),color="g")
plt.show()


# In[41]:


player_salary = fifa[["short_name","wage_eur"]]


# In[42]:


player_salary.head()


# In[46]:


plt.figure(figsize=(8,5))
plt.bar(list(player_salary["short_name"])[0:5],list(player_salary["wage_eur"])[0:5],color="r")
plt.show()

