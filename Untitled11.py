#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[124]:


import os 


# In[125]:


os.listdir(r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets")


# In[126]:


uber = pd.read_csv(r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets\uber-raw-data-janjune-15_sample.csv")


# In[127]:


uber


# In[128]:


uber.shape


# In[129]:


type(uber)


# In[130]:


uber.duplicated().sum()


# In[131]:


uber.drop_duplicates(inplace=True)

uber.duplicated().sum()
# In[132]:


uber.shape


# In[133]:


uber.dtypes


# In[134]:


uber.isnull().sum()


# In[135]:


uber['Pickup_date'][0]


# In[136]:


type(uber['Pickup_date'][0])


# In[137]:


uber['Pickup_date']= pd.to_datetime(uber['Pickup_date'])


# In[138]:


type(uber['Pickup_date'][0])


# In[139]:


uber.dtypes


# In[140]:


uber


# In[141]:


uber['Month'] = uber['Pickup_date'].dt.month_name()


# In[142]:


uber['Month']


# In[143]:


uber['Month'].value_counts().plot(kind='bar')


# In[144]:


uber['WeekDay'] = uber['Pickup_date'].dt.day_name()
uber['Day'] = uber['Pickup_date'].dt.day
uber['Hour']  = uber['Pickup_date'].dt.hour
uber['Minute'] = uber['Pickup_date'].dt.minute


# In[145]:


uber.head()


# In[146]:


pivot_table = pd.crosstab(index=uber['Month'] , columns =uber['WeekDay'] )


# In[147]:


pivot_table


# In[148]:


pivot_table.plot(kind="bar" , figsize=(8,6),title ="Max Uber Pickups in New York City by month and Days" )


# In[149]:


summary = uber.groupby(['WeekDay' , 'Hour'], as_index=False).size()


# In[150]:


summary


# In[151]:


plt.figure(figsize(8,6))
sns.pointplot(x="Hour",y="size",hue="WeekDay",data=summary)


# In[152]:


uber.columns


# In[153]:


os.listdir(r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets")


# In[154]:


uber_foil = pd.read_csv(r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets\Uber-Jan-Feb-FOIL.csv")


# In[155]:


uber_foil


# In[156]:


uber_foil.shape


# In[157]:


get_ipython().system('pip install chart_studio')
get_ipython().system('pip install plotly')


# In[158]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot


# In[159]:


uber_foil.columns


# In[160]:


px.box(x='dispatching_base_number' , y='active_vehicles' , data_frame=uber_foil)


# In[161]:


px.violin(x='dispatching_base_number' , y='active_vehicles' , data_frame=uber_foil)


# In[162]:


files = os.listdir(r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets")[-8:]


# In[163]:


files


# In[164]:


files.remove('uber-raw-data-janjune-15.csv')


# In[165]:


files


# In[166]:


files.remove('uber-raw-data-janjune-15_sample.csv')


# In[167]:


files


# In[168]:


final = pd.DataFrame()
path =  r"C:\Users\kisha\OneDrive\Desktop\DOCUMENTS\data analyst\projects\Datasets"
for file in files : 
    current_df = pd.read_csv(path+'/'+file)
    final = pd.concat([current_df,final])


# In[169]:


final.shape


# In[170]:


final.duplicated().sum()


# In[171]:


final.drop_duplicates(inplace=True)


# In[172]:


final.shape


# In[173]:


final.head(3)


# In[174]:


rush_uber = final.groupby(['Lat','Lon'],as_index = False).size()


# In[175]:


rush_uber


# In[176]:


get_ipython().system('pip install folium')


# In[177]:


import folium


# In[178]:


basemap = folium.Map()


# In[179]:


from folium.plugins import HeatMap


# In[180]:


HeatMap(rush_uber).add_to(basemap)


# In[181]:


basemap


# In[182]:


final.columns


# In[183]:


final.head()


# In[184]:


final.dtypes


# In[188]:


final['Date/Time'] = pd.to_datetime(final['Date/Time'],format ="%m/%d/%Y %H:%M:%S")


# In[190]:


final['Date/Time'].dtype


# In[193]:


final['Day']=final['Date/Time'].dt.day
final['Hour']=final['Date/Time'].dt.hour


# In[194]:


final.head()


# In[199]:


pivot = final.groupby(['Day','Hour']).size().unstack()


# In[200]:


pivot


# In[201]:


pivot.style.background_gradient()


# In[202]:


def gen_pivot_table(df,col1,col2):
    pivot = final.groupby(['Day','Hour']).size().unstack()
    return pivot.style.background_gradient()


# In[203]:


final.columns


# In[204]:


gen_pivot_table(final , "Day" , "Hour")


# In[ ]:




