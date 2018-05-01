
# coding: utf-8

# In[2]:


get_ipython().magic('pylab inline')


# In[2]:


import sys
import csv
import math
import folium
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geojson
from scipy import stats

get_ipython().magic('matplotlib inline')
data4 = pd.read_csv("/home/elena/Documents/DataMining/Data/ElectionData/presidential_general_elections/data/tonmcg/16.csv")
data5 = pd.read_csv("/home/elena/Documents/DataMining/Data/CleanedCSVs/2015Cluster.csv")
data6 = pd.read_csv("/home/elena/Downloads/us_postal_codes.csv")



# In[3]:



data4.head(6)



# In[4]:


data5.head()


# In[5]:


data4.margin_winner_over_runnerup.describe()


# In[ ]:


data6 = data6.rename(columns={'Zip Code': 'zipcode'})
data6 = data6.rename(columns={'State': 'state'})
data6.head()


# In[ ]:


left = data5
right = data6 
#result = left.join(right, on='zipcode')
result = data5.merge(data6, on='zipcode', how='left')
result.head()


# In[326]:


clusterState = pd.DataFrame(result.groupby('state').agg(lambda x:x.value_counts().index[0]))
clusterState.head() 


# In[336]:


def binning(col, cut_points, labels=None):
  #Define min and max values:
  minval = col.min()
  maxval = col.max()

  break_points = [minval] + cut_points + [maxval]

  if not labels:
    labels = range(len(cut_points)+1)
  colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
  return colBin

cut_points = [13,39]
labels = ["low","medium","high"]
data4["Homogeny"] = binning(data4["margin_winner_over_runnerup"], cut_points, labels = ["low","medium","high"])
pd.value_counts(marginData["margin_winner_over_runnerup"], sort=False)
data4.Homogeny.apply(str)
data4.head()


# In[341]:


polarity = []


# For each row in the column,
for index, row in data4.iterrows():
    if (row.Homogeny == "high") & (row.winner == "rep"):
        polarity.append('Very Republican')
    elif (row.Homogeny  == "medium") & (row.winner  == "rep"):
        polarity.append('Moderately Republican')
    elif (row.Homogeny  == "low") & (row.winner  == "rep"):
        polarity.append('Slighty Republican')
    elif (row.Homogeny  =="high") & (row.winner  == "dem"):
        polarity.append('Very Democrat')
    # else, if more than a value,
    elif (row.Homogeny  == "medium")&(row.winner  == "dem"):
        polarity.append('Moderately Democrat')
    # else, if more than a value,
    elif (row.Homogeny  == "low") &  (row.winner  == "dem"):
        # Append a letter grade
        polarity.append('Slightly Democrat')
        
# Create a column from the list
data4['polarity'] = polarity 
data4.head()


# In[ ]:


data4.pct_rep.describe()


# In[342]:


marginData = pd.DataFrame(data4.groupby('State Abbreviation')['margin_winner_over_runnerup'].mean())
marginData.head()


# In[81]:


marginData.describe()


# In[344]:


def binning(col, cut_points, labels=None):
  #Define min and max values:
  minval = col.min()
  maxval = col.max()

  break_points = [minval] + cut_points + [maxval]

  if not labels:
    labels = range(len(cut_points)+1)
  colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
  return colBin

cut_points = [13,39]
labels = ["low","medium","high"]
marginData["Margins Bin"] = binning(marginData["margin_winner_over_runnerup"], cut_points, labels = ["low","medium","high"])
pd.value_counts(marginData["margin_winner_over_runnerup"], sort=False)
marginData.head()



# In[ ]:



    


# In[345]:


left = result
right = marginData 
resultF = left.join(right, on='State Abbreviation')
resultF.head()

resultF = result.merge(marginData, on='State Abbreviation', how='left')
resultF.head()
# In[ ]:


resultF.plot.scatter("avg_agi", "margin_winner_over_runnerup", s=.4, c = "magenta")


# In[ ]:


resultF.plot.bar(x= "Cluster", y ="margin_winner_over_runnerup")


# In[ ]:





# In[ ]:




