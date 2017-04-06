
# coding: utf-8

# In[ ]:




# In[2]:

import pandas as pd
import os
import datetime
import numpy as np
import calendar


# In[3]:

df = pd.read_csv('vehicle_collisions.csv',parse_dates=['DATE'],infer_datetime_format=True)


# In[4]:

#df=df.replace(np.nan, '', regex=True)
df.columns = [c.replace(' ', '_') for c in df.columns]


# In[5]:

df.head()


# In[6]:

#df.BOROUGH.notnull()


# In[7]:

df[df.BOROUGH=='MANHATTAN'].notnull().sum()


# In[9]:

#testing for getting only the output where Borough = Queens
manhattan_data=df[df.BOROUGH=='QUEENS']


# In[11]:

manhattan_data.head()


# In[12]:

type(manhattan_data.VEHICLE_1_TYPE.dropna())


# In[18]:

data1=pd.DataFrame(columns=['Origin','One Vehicle Involved','Two Vehicle Involved','Three Vehicle Involved','More Vehicle Involved'])


# In[19]:

#excluding the data which has no Borough, counting all the accidents involving different count of vehicles
for origin in df.BOROUGH.unique():
    #print(origin)
    if not pd.isnull(origin):
        #print(origin)
        manhattan_data=df[df.BOROUGH==origin]
        two_vehicles=str(manhattan_data[(manhattan_data.VEHICLE_1_TYPE.notnull()) & (manhattan_data.VEHICLE_2_TYPE.notnull())&(manhattan_data.VEHICLE_3_TYPE.isnull())&(manhattan_data.VEHICLE_4_TYPE.isnull())&(manhattan_data.VEHICLE_5_TYPE.isnull())].shape[0])
        one_vehicle= str(manhattan_data[(manhattan_data.VEHICLE_1_TYPE.notnull()) & (manhattan_data.VEHICLE_2_TYPE.isnull())&(manhattan_data.VEHICLE_3_TYPE.isnull())&(manhattan_data.VEHICLE_4_TYPE.isnull())&(manhattan_data.VEHICLE_5_TYPE.isnull())].shape[0])
        three_vehicle=str(manhattan_data[(manhattan_data.VEHICLE_1_TYPE.notnull()) & (manhattan_data.VEHICLE_2_TYPE.notnull())&(manhattan_data.VEHICLE_3_TYPE.notnull())&(manhattan_data.VEHICLE_4_TYPE.isnull())&(manhattan_data.VEHICLE_5_TYPE.isnull())].shape[0])
        more_vehicles=str(manhattan_data[(manhattan_data.VEHICLE_1_TYPE.notnull()) & (manhattan_data.VEHICLE_2_TYPE.notnull())&(manhattan_data.VEHICLE_3_TYPE.notnull())&(manhattan_data.VEHICLE_4_TYPE.notnull())&(manhattan_data.VEHICLE_5_TYPE.isnull())].shape[0]+manhattan_data[(manhattan_data.VEHICLE_1_TYPE.notnull()) & (manhattan_data.VEHICLE_2_TYPE.notnull())&(manhattan_data.VEHICLE_3_TYPE.notnull())&(manhattan_data.VEHICLE_4_TYPE.notnull())&(manhattan_data.VEHICLE_5_TYPE.notnull())].shape[0])
        #dataFrame = pd.DataFrame(data=[origin,one_vehicle,two_vehicles,three_vehicle,more_vehicles])
        #data1.append(dataFrame,ignore_index=True)
        #print(one_vehicle)
        data1 = data1.append(pd.Series([origin,one_vehicle,two_vehicles,three_vehicle,more_vehicles],index=['Origin','One Vehicle Involved','Two Vehicle Involved','Three Vehicle Involved','More Vehicle Involved']),ignore_index=True)
        #columns={'Origin': origin,'One Vehicle Involved':one_vehicle,'Two Vehicle Involved':two_vehicles,'Three Vehicles Involved':three_vehicle,'More Vehicle Involved':more_vehicles}


# In[20]:

data1.head()


# In[21]:

data1.to_csv(path_or_buf=os.path.join(os.getcwd(),'Q1P2.csv'))


# In[ ]:




# In[ ]:



