
# coding: utf-8

# In[13]:

import pandas as pd
import os
import datetime
import numpy as np


# In[14]:

df = pd.read_csv('cricket_matches.csv')


# In[15]:

df.head(10)


# In[ ]:




# In[16]:

#taking only columns where the host has won the game
truth= df['home'] == df['winner']
data = df[truth]


# In[17]:

data.head()


# In[18]:

df[df.home==df.winner]
#using ternary operations and creating a runs column having the runs scored by the winner of the match
df['runs'] = np.where(pd.isnull(df['win_by_runs']), df['innings2_runs'], df['innings1_runs'])


# In[19]:

df['runs'].head(10)


# In[20]:

df[truth]


# In[21]:

#taking mean of the runs of each team
data_output=df[truth].groupby('home').agg({'runs':np.mean})


# In[22]:

data_output.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q3.csv'))


# In[23]:

data_output.head()


# In[ ]:



