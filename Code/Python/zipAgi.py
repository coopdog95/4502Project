
import pandas as pd
import numpy as np
import sys

df = pd.read_csv("zipLatLon.csv") #dataframe containing all Lats/Longs

'''		df

zip - Lat - Long

'''

print("Lat-Long file read successfully.")

yearr = sys.argv[1]
agi = int(sys.argv[2])
dfYear = pd.read_csv("FIX" + yearr + "zip.csv") #year-specific dataframe 


'''		dfYear

zip - agi_stub - n1

'''
print("Yearly data read successfully")



##### CLEANING #######


rep = input("Is desired agi smaller than the agi you passed in? ")
if(rep == "y"):
	print("Ok, will change.")
	#dfYear = dfYear[dfYear['agi_stub'] < agi]
	dfYear['n1'] = dfYear['n1']*(7/6)
	agi -= 1

dfYear = dfYear[dfYear['agi_stub'] <= agi]
dfYear = dfYear[dfYear['agi_stub'] >= 1]
dfYear = dfYear[dfYear['zipcode'] > 0]
dfYear = dfYear[dfYear['zipcode'] != 99999]



print("Value Counts: \n")
print(dfYear['agi_stub'].value_counts())


dfYear.reset_index(drop=True, inplace=True)


rep2 = input("Type anything to continue.")
if(len(rep2) == 0):
	exit()


print("\n\n")


rep3 = input("Type anything to clean. Type Enter to skip cleaning.")
if(len(rep3) != 0):
	a = 0
	b = agi
	count = 0

	while a < dfYear['zipcode'].count():
		if(dfYear['agi_stub'][a:b].max() != agi):
			#print("Entered 1")
			#print("a = ", a)
			#print(dfYear[a:b]) 
			badZip = dfYear['zipcode'][a]
			dfYear = dfYear.drop(dfYear[dfYear.zipcode == badZip].index)
			dfYear.reset_index(drop=True, inplace=True)
			print("  ", badZip, "bad zipcode!")
			count += 1
			if(count%100 == 0):
				print("Count = ", count)
			#b += agi
		elif(dfYear['agi_stub'][b-1] != agi):
			#print("Entered 2")
			#print("a = ", a)

			#print("heres the head")
			#print(dfYear.head(10))
			#print("followed by a:b")
			#print(dfYear[a:b]) 
			badZip = dfYear['zipcode'][a]
			dfYear = dfYear.drop(dfYear[dfYear.zipcode == badZip].index)
			dfYear.reset_index(drop=True, inplace=True)
			print("  ", badZip, "bad zipcode!")
			count += 1
			if(count%100 == 0):
				print("Count = ", count)
			#b += agi
		elif(dfYear['agi_stub'][a:b].sum() != 21):
			badZip = dfYear['zipcode'][a]
			print("  ", badZip, "bad zipcode!")
			dfYear = dfYear.drop(dfYear[dfYear.zipcode == badZip].index)
			dfYear.reset_index(drop=True, inplace=True)
	#print("  ", badZip, "bad zipcode!")
			count += 1
			if(count%100 == 0):
				print("Count = ", count)
		else:
			a += agi
			b += agi

	print("There were", count, "bad zipcodes!")

	print("Here are the value counts now..")

	print(dfYear['agi_stub'].value_counts())

response = input("Does this look good?")

if(response == "y"): #TYPING Y (YES) HERE WILL WRITE TO THE FILE! 

	print("Now multiplying...")

	def Multipl(x):
	        return x['agi_stub']*x['n1']

	dfYear['multiplied'] = dfYear.apply(Multipl, axis=1)

	rangy = int(dfYear['zipcode'].count()/agi) 

	newDF = pd.DataFrame(index=range(rangy),columns=['zipcode','avg_agi']) 

	newDF['zipcode'] = list(dfYear['zipcode'][::agi]) #filling newDF with all zipcodes straight from year-specific dataframe

	inde = 0
	st = 0
	end = agi

	print("Now finding avg_agi for each zip...")

	max_rows = dfYear['zipcode'].count()

	while st < max_rows:
	    try:
	        newDF.loc[inde, 'avg_agi'] = dfYear['multiplied'][st:end].sum()/(dfYear['n1'][st:end].sum()) #formula to calculate list of avg_agi
	        st += agi
	        end += agi
	        inde += 1
	        
	    except ZeroDivisionError:
	        newDF.loc[inde, 'avg_agi'] = 0.0 
	        st += agi
	        end += agi
	        inde += 1

	#if(agi == 7):
	#	newDF['avg_agi'] = newDF['avg_agi']*(6/7)



	print("Now merging...")

	result = pd.merge(df, newDF, on='zipcode') #final dataframe with all desired fields

	print(result.head(20))

	result.to_csv("avg_agis/" + yearr + "agi.csv", index=False)

	print("File complete!\n")


else:
	print("goodbye")
