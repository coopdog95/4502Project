import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()
#zipcode = search.by_zipcode("10001")
#zip2 = search.by_zipcode(data['zipcode'][0])
#print(zip2.Latitude)

data = pd.read_csv("FIX2005zip.csv")

df = pd.DataFrame(list(data['zipcode'].unique()), columns=["zipcode"])
df = df.drop(df.index[:261]).reset_index(drop=True)

def zipToLatitude(x):
	latt = search.by_zipcode(int(x))['Latitude']
	return latt

def zipToLongitude(x):
	longg = search.by_zipcode(int(x))['Longitude']
	return longg


df['nulll'] = df['zipcode'].apply(lambda x: 'yes' if zipToLatitude(x) == None else 'no') #add null? column to identify zips without weird responses..

df = df.drop(df[df['nulll'] == 'yes'].index).reset_index(drop=True) #delete every entry where this is true

print("DataFrame before null column delete")
print(df.head(40))


df = df.drop('nulll', 1)
print("DataFrame after null column delete")
print(df.head(40))



df.to_csv("zips.csv", index=False)