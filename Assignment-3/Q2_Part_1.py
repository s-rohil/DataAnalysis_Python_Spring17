
# coding: utf-8

# In[2]:

import pandas as pd
import os
import datetime
import numpy as np


# In[3]:

df = pd.read_csv('employee_compensation.csv')


# In[4]:

df.head()


# In[5]:

df.columns = [c.replace(' ', '_') for c in df.columns]


# In[6]:

data = df.groupby(['Organization_Group','Department'], as_index=False)['Total_Compensation'].mean()


# In[7]:

data.head(10)


# In[8]:

new_data=data.sort_values(by=['Organization_Group','Total_Compensation'],ascending=[True,False])
#new_data.head(10)


# In[9]:

new_data.head(10)


# In[10]:

#test=df.groupby(['Organization_Group','Department']).agg({'Total_Compensation':np.mean})


# In[11]:

new_data.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q2P1.csv'))


# In[13]:

# printing the top Department of each Organization Group with the highest compensation
best_dept=new_data.sort_values('Total_Compensation', ascending=False).groupby('Organization_Group', as_index=False).first()


# In[14]:

best_dept.head(7)


# In[ ]:



