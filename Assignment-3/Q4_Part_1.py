
# coding: utf-8

# In[518]:

import pandas as pd
import os
import datetime
import numpy as np
import re


# In[519]:

df = pd.read_csv('movies_awards.csv')


# In[520]:

df.head()


# In[521]:

df.columns = [c.replace(' ', '_') for c in df.columns]


# In[522]:

data=pd.DataFrame(df,columns=['Awards'])


# In[523]:

data.head()


# In[524]:

list=[]
for award in df.Awards.unique():
    if not pd.isnull(award):
        list.append(award)
# Creating a new dataframe with only the Awards column
data1=pd.DataFrame(list,columns=['Awards'])


# In[525]:

data1['Awards'] = data1['Awards'].str.lower()


# In[526]:

data1.head()


# In[527]:

#split the column into 2 using '.' as delimiter
temp = pd.DataFrame(data1.Awards.str.split('.').tolist())


# In[528]:

temp.head(15)
temp.fillna(value=0, inplace=True)
temp.head()


# In[529]:

#taking the first column from temp and splitting on &
temp0 = pd.DataFrame(temp[0].str.split('&').tolist())


# In[530]:

temp0.head()


# In[531]:


# using the 0th column of the dataframe temp0 after split on . and & for preparing the output
# making dataframe of specific keywords used for further processing
bafta=pd.DataFrame(temp0[0][temp0[0].str.contains(('bafta'), regex=True)])
globes=pd.DataFrame(temp0[0][temp0[0].str.contains(('golden'), regex=True)])
oscar=pd.DataFrame(temp0[0][temp0[0].str.contains(('oscar'), regex=True)])
wins=pd.DataFrame(temp0[0][temp0[0].str.contains(('win|wins|won'), regex=True)])
nominates=pd.DataFrame(temp0[0][temp0[0].str.contains(('nomin'), regex=True)])
emmy=pd.DataFrame(temp0[0][temp0[0].str.contains(('emmy'), regex=True)])
only_wins=(pd.DataFrame(temp0[0][~temp0[0].str.contains('emmy|oscar|bafta|golden|nomin')]))
only_nominations=(pd.DataFrame(temp0[0][~temp0[0].str.contains('emmy|oscar|bafta|golden|win|wins|won')]))
#data1['win']=temp0[0].str.extract('(\d)', expand=True)


# In[532]:

nominates.head(10)


# In[533]:

#nominates.merge(bafta, how='inner', left_index=True, right_index=True)


# In[534]:

#joining nomination/wins with the respective awards and then extracting the number from the column
data1['Nominated_BAFTA']= nominates.join(bafta, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[535]:

data1['Winner_BAFTA']=wins.join(bafta, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[536]:

data1['Winner_OSCAR']=wins.join(oscar, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[537]:

data1['Nominated_OSCAR']=nominates.join(oscar, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[538]:

data1['Winner_Emmy']=wins.join(emmy, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[539]:

data1['Nominated_Emmy']=nominates.join(emmy, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[540]:

data1['Winner_Globes']=wins.join(globes, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[541]:

data1['Nominated_Globes']=nominates.join(globes, how='inner',lsuffix='test')['0'].str.extract('(\d{1,3})', expand=True)


# In[542]:

data1['Awards_Won']=only_wins[0].str.extract('(\d{1,3})', expand=True)


# In[543]:

data1.head()


# In[544]:

#taking the second column from temp and splitting on &
temp1 = pd.DataFrame(temp[1].str.split('&').tolist())


# In[545]:

#Part 2/6th of getting the output
data1['Nominations']=temp0[1].str.extract('(\d{1,3})', expand=True)


# In[546]:

data1.Nominations.fillna(only_nominations[0].str.extract('(\d{1,3})', expand=True)[0], inplace=True)


# In[547]:

data1.head()


# In[548]:

temp1.head(15)
temp1.fillna(value='', inplace=True)


# In[549]:

#part3 and 4 of getting the output. Working with sub-columns of column '1' of df temp after splitting on '&'

only_wins1=(pd.DataFrame(temp1[0][~temp1[0].str.contains('emmy|oscar|bafta|golden|nomin')]))
only_nominations1=(pd.DataFrame(temp1[0][~temp1[0].str.contains('emmy|oscar|bafta|golden|win|wins|won')]))
only_nominations11=(pd.DataFrame(temp1[1][~temp1[1].str.contains('win|wins|won')]))
#data1['Nominations']=temp0[1].str.extract('(\d)', expand=True)
data1.Nominations.fillna(only_nominations1[0].str.extract('(\d{1,3})', expand=True)[0], inplace=True)
data1.Nominations.fillna(only_nominations11[1].str.extract('(\d{1,3})', expand=True)[0], inplace=True)
data1.Awards_Won.fillna(only_wins1[0].str.extract('(\d{1,3})', expand=True)[0], inplace=True)


# In[550]:

data1.head()


# In[551]:

data1=data1.fillna(0)


# In[552]:

data1.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q4.csv'))


# In[ ]:



