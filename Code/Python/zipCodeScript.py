import pandas as pd
import numpy as np
import sys


filename = sys.argv[1]
outFile = sys.argv[2]

fixstring = "FIX"

newFileName = fixstring + outFile


data = pd.read_csv(filename, low_memory=False)

data.columns = data.columns.str.lower()

fixData = data[["zipcode","agi_class",'n1']]

'''
try:
	fixData = data[["zipcode","AGI_STUB",'N1']]
except:
	fixData = data[["ZIPCODE","AGI_STUB",'N1']]
else:
	fixData = data[["zipcode","agi_stub",'N1']]
finally:
	fixData = data[["ZIPCODE","agi_stub",'N1']]
'''



fixData.to_csv("fixed/" + newFileName, index=False)
