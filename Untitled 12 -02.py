#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install matplotlib')


# In[5]:


get_ipython().system('pip install seaborn')


# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("fake_news.csv")
data.head()


# In[12]:


data.shape


# In[7]:


data.info()


# In[8]:


data = data.drop(['id'],axis = 1)


# In[9]:


data.isna().sum()


# In[19]:


data = data.fillna('')


# In[20]:


data['content'] = data['author']+' '+data['title']+" "+data['text']


# In[ ]:


data = data.drop(['title','author','text'],axis = 1)


# In[16]:


data.head()


# In[ ]:


data['content'] = data['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))


# In[ ]:


data['content'] = data['content'].str.replace('[^\w\s]','')


# In[21]:


import nltk
nltk.download('stopwords')


# In[ ]:




