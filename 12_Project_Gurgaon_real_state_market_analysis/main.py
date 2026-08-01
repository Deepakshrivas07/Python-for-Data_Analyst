import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
#NOTE 1st checking the colums formats and datatypes
df.columns = df.columns.str.lower().str.replace(' ','_').str.strip()
# print(df.info())
# print(df.head())


# NOTE 2nd column cleaning
 
## numerical data cleaning
df['price'] = df['price'].str.replace(',','').astype(float)
df['rate_per_sqft'] = df['rate_per_sqft'].str.replace(',','').astype(int)


## cetegorical cloumns cleaning
df['status']=df['status'].str.lower().str.strip()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera':True,'not approved by rera':False})    
df['flat_type'] = df['flat_type'].str.strip().str.lower()
# print(df[["rera_approval"]])
# NOTE 3rd droping dublicates
df.drop_duplicates()
# print(df.isna().sum()) # checking for empty values

# NOTE 4th replace all inconsistent symbol of missing values into one single symbol
# df = df.replace(["-", "none", "NULL", "?", "N/A"],"NA")
# print(df.info())

#QUESTIONS
#Question 1: Which is the costliest flat?
costiest_flat  = df['price'].idxmax()
# print(costiest_flat) it will print the index of costliest flat but our que is Which is the costliest flat?
print(df.loc[costiest_flat])