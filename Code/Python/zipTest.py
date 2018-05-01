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

df = pd.read_csv("zips.csv")

def zipToLatitude(x):
	latt = search.by_zipcode(int(x))['Latitude']
	return latt

def zipToLongitude(x):
	longg = search.by_zipcode(int(x))['Longitude']
	return longg

df['latitude'] = df['zipcode'].apply(lambda x: zipToLatitude(x) if not(96898 > x > 96701) else np.nan)
df['longitude'] = df['zipcode'].apply(lambda x: zipToLongitude(x) if not(96898 > x > 96701) else np.nan)

df = df[np.isfinite(df['latitude'])]

df.to_csv("zipLatLon.csv", index=False)


print(df.head(100))