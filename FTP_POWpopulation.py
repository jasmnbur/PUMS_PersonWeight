#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[22]:


df = pd.read_csv(r'/Users/jburesch/Desktop/psam_p36.csv', nrows = 50)


# In[23]:


df


# In[24]:


df['POWPUMA']


# In[25]:


df[df['POWPUMA'].notnull()]


# In[27]:


column_sum = df['PWGTP'].sum()


# In[29]:


print(column_sum)


# In[ ]:




