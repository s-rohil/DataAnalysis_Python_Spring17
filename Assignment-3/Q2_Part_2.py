
# coding: utf-8

# In[ ]:




# In[1]:

import pandas as pd
import os
import datetime
import numpy as np
import calendar


# In[2]:

df = pd.read_csv('employee_compensation.csv')


# In[3]:

df.head(15)


# In[4]:

df.columns = [c.replace(' ', '_') for c in df.columns]


# In[5]:

dataset=df.groupby(['Year','Employee_Identifier']).agg({'Total_Salary':np.mean, 'Retirement':np.mean,'Health/Dental':np.mean,'Other_Benefits':np.mean,'Total_Benefits':np.mean,'Total_Compensation':np.mean})


# In[6]:

dataset.head(6)


# In[7]:

df[df.Overtime>0.05*(df.Salaries)].Employee_Identifier.head()


# In[8]:

output=df.groupby('Job_Family').agg({'Total_Benefits':np.mean, 'Total_Compensation':np.mean})


# In[9]:

output.head()


# In[10]:

output['percentage']=(output.Total_Benefits/output.Total_Compensation)*100


# In[11]:

output.head()


# In[12]:

output.sort_values(by='percentage',ascending=False).head(5)


# In[13]:

output.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q2P2.csv'))


# In[ ]:



