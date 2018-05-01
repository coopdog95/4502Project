import pandas as pd
import numpy as np
import sys

yearr = sys.argv[1]

df = pd.read_csv("csvs/" + yearr + "Cluster.csv")

dfM = pd.read_csv("Master2.csv")

print("Master file read successfully. Here it is:\n") ####READ IN MASTER FILE
print(dfM.head(10))


rep = input("Does this look ok? ")

if(rep == "y"):


	df = df[['zipcode', 'Cluster']]
	#df = df.astype(int)

	dfM = dfM.merge(df, on='zipcode', how='left') ##MERGE COLUMNS

	count = dfM['Cluster'].value_counts().min()

	print("Before merging there were", count, "zeros")

	dfM['Cluster'] = dfM['Cluster'].replace(np.inf, 0)
	dfM['Cluster'] = dfM['Cluster'].replace(np.nan, 0)
	dfM['Cluster'] = dfM['Cluster'].astype(int)

	count = dfM['Cluster'].value_counts().min()
	print("After merging there are", count, "zeros")

	dfM = dfM.rename(columns={"Cluster": yearr}) ###RENAME NEW COLUMN TO YEAR

	print("Column added. Here it is.")
	print(dfM.head(10))

	rep2 = input("Look good? ")
	if(rep2 == "y"):

		dfM.to_csv("Master2.csv",index=False)  ##WRITE TO NEW FILE

	else:
		print("damn aight. no new filez\n")
		exit()



else:
	print("seeyuh\n")
	exit()
