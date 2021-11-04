#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r'/Users/jburesch/Desktop/psam_p36.csv')


# In[3]:


column_sum = df['PWGTP'].sum()


# In[4]:


print(column_sum)


# In[13]:


df2 = df[df['POWPUMA'].notnull()]


# In[47]:


df2.head(15)


# In[48]:


df2[['PUMA', 'POWPUMA','PWGTP']].head(15)


# In[49]:


df2['PUMA']=df2['PUMA'].astype(str)

empty_list_1 = []
empty_list_2 = []
empty_list_3 = []

# puma_number = str(input('Please enter the PUMA you want to search: '))


def search_PUMA(x):
#     global puma_number
## used my previous code to find PUMAs in Harlem, Manhattan & entered relevant PUMAs
    if x['PUMA'] == '3802' or x['PUMA'] == '3803' or x['PUMA'] == '3804':
        empty_list_1.append(x['PUMA'])
        empty_list_2.append(x['POWPUMA'])
        empty_list_3.append(x['PWGTP'])

df2.apply(search_PUMA, axis=1)

df3 = pd.DataFrame({
    'PUMA':empty_list_1,
    'POWPUMA':empty_list_2,
    'PWGTP':empty_list_3
})

df3.head(15)


# In[50]:


# Summing person weights
column_sum3 = df3['PWGTP'].sum()


# In[51]:


# RESULT: There was a total of 188,939 persons who's place of work was within the neighborhoods of Harlem in 2019
print(column_sum3)


# In[56]:


df3.to_excel('POW_PUMA.xlsx', engine='xlsxwriter')


# In[ ]:




