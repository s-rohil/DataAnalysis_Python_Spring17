
# coding: utf-8

# In[ ]:




# In[1]:

import pandas as pd


# In[2]:

import os
import datetime
import numpy as np


# In[3]:

import calendar


# In[4]:




# In[5]:

df = pd.read_csv('vehicle_collisions.csv',parse_dates=['DATE'],infer_datetime_format=True)


# In[6]:

df.columns = [c.replace(' ', '_') for c in df.columns]
df.head(3)


# In[7]:

#converting DATE column to datetime datatype and taking entries of only the year 2016
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y',errors='ignore')
df = df[(df.DATE.dt.year==2016)]


# In[8]:

#taking only entries of Manhattan and the year 2016
data = df[(df.BOROUGH=='MANHATTAN') & (df.DATE.dt.year==2016)]


# In[9]:

data.head()



# In[15]:

man_data=data.groupby([data.DATE.dt.month])['UNIQUE_KEY'].count()


# In[16]:

nyc_data=df.groupby([df.DATE.dt.month])['UNIQUE_KEY'].count()


# In[17]:

percentage=man_data/nyc_data


# In[20]:

#taking the month_name to be used in the dataframe
month_dict={n: {} for n in range(1,13)}
for i in range(1,13):
    month_dict[i]=calendar.month_name[i]


# In[21]:

#taking list of columns for preparing the dataframe
data=[month_dict,man_data,nyc_data,percentage]


# In[22]:

dataframe = pd.DataFrame.from_records(data,index=['Month','Manhattan','NYC','Percentage']).transpose()


# In[23]:

dataframe.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q1P1.csv'))


# In[24]:




# In[ ]:



