#!/usr/bin/env python
# coding: utf-8

# In[248]:


import pandas as pd
import re

#read a comma-separated values (csv) file into dataframe
df = pd.read_csv('loyalty.csv')
df1 = pd.read_csv('transactions.csv')


# In[249]:


#return the first seven rows of the dataframe
df.head(7)
df1.head(7)

#return a tuple representing the dimensionality of the dataframe
df.shape
df1.shape


# In[250]:


#return the column labels of the dataframe
df.columns
df1.columns


# In[251]:


#rename the column labels of the dataframe
df.columns = ['name','city','phone_number','license_plate','email','id']
df1.columns = ['name','city','phone_number','email','id','Transaction_ID','Amount']


# In[252]:


#return the new column labels of the dataframe
df.columns
df1.columns


# In[253]:


#return the first seven rows of the dataframe
df.head(7)
df1.head(7)


# In[254]:


#apply uppercase to the columns in dataframe
df.columns = [x.upper() for x in df.columns]
df.columns
df1.columns = [x.upper() for x in df1.columns]
df1.columns


# In[255]:


#return the first seven rows of the dataframe
df.head(7)
df1.head(7)


# In[256]:


#returns a string where all characters are lowercase 
df['EMAIL'] = df['EMAIL'].apply(lambda x: x.lower())
df.head(7)
df1['EMAIL'] = df1['EMAIL'].apply(lambda x: x.lower())
df1.head(7)


# In[257]:


#data cleansing - removal of special characters and necessary spaces from the dataframe
df['NAME'] = df['NAME'].str.replace(r"[^a-zA-Z ]+", "")
df['CITY'] = df['CITY'].str.replace(r"[^a-zA-Z ]+", "")
df['PHONE_NUMBER'] = df['PHONE_NUMBER'].str.replace(r"[^0-9]+", "")
df['LICENSE_PLATE'] = df['LICENSE_PLATE'].str.replace(r"[^a-zA-Z0-9]+", "")
df['EMAIL'] = df['EMAIL'].str.replace(r"[^a-zA-Z0-9._@]+", "")
df['ID'] = df['ID'].str.replace(r"[^a-zA-Z0-9-]+", "")


# In[258]:


#data cleansing - removal of special characters and necessary spaces from the dataframe
df1['NAME'] = df1['NAME'].str.replace(r"[^a-zA-Z ]+", "")
df1['CITY'] = df1['CITY'].str.replace(r"[^a-zA-Z ]+", "")
df1['PHONE_NUMBER'] = df1['PHONE_NUMBER'].str.replace(r"[^0-9]+", "")
df1['EMAIL'] = df1['EMAIL'].str.replace(r"[^a-zA-Z0-9._@]+", "")
df1['ID'] = df1['ID'].str.replace(r"[^a-zA-Z0-9-]+", "")


# In[259]:


#return the first seven rows of the dataframe
df.head(7)
df1.head(7)


# In[260]:


#merge dataframe with a database-style join
df3 = pd.merge(df,df1,on=['NAME','CITY','PHONE_NUMBER','EMAIL','ID'])


# In[261]:


#return the column labels of the dataframe
df3.columns


# In[262]:


#return the first seven rows of the dataframe
df3.head(7)


# In[263]:


#return a tuple representing the dimensionality of the dataframe
df3.shape


# In[264]:


#write dataframe to a comma-separated values (csv) file
df3.to_csv("C:\\Users\\Lithiya Letchumy\\Desktop\\SunwayGroupTest\\Merged_Loyalty_Transaction.csv",index=False)


# In[ ]:




