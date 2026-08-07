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
costiest_flat  = df['price'].idxmax() #idxmax gives index of max value and as we know loc takes row as index and column as value
df.loc[costiest_flat]
#print(costiest_flat) #it will print the index of costliest flat but our que is Which is the costliest flat?

# or we can write in single line 
costiest_flat = df.loc[df['price'].idxmax(),'property_type'] 
print(costiest_flat)
# Question 2: Which locality has the highest average price?

highest_avg_price=  df.groupby('locality')['price'].mean().sort_values(ascending=False).head(1)
# print(highest_avg_price)

#Question 3: Which locality has the highest rate per square foot?

highest_rate_per_sqfoot = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False).head(1)
# print(highest_rate_per_sqfoot)

#Question 4: Ready-to-move vs Under-construction pricing
ready_vs_under_construction =df.groupby('status')['price'].median() #(optimal as u can see below 3 line code)
# print(ready_vs_under_construction)
#or (non optimal)
under_contruction_price = df[df['status']=='under construction']['price'].median()
ready_to_move_price = df[df['status']=='ready to move']['price'].median()
# print(under_contruction_price)
# print(ready_to_move_price)

#Question 5: Does RERA approval affect pricing?
rera_approval=df.groupby("rera_approval")["price"].median()
#or
rera_approval_true = df[df['rera_approval']=='True']['price'].median()
rera_approval_false = df[df['rera_approval']=='False']['price'].median()
# print(rera_approval)

#Question 6: How does area impact price?
# let see by plotting
# sns.scatterplot(x='area',y='price',data=df)
# plt.show() #ans is no location affects the price not area

#Question 7: Which BHK configuration is most expensive? 
most_expensive_bhk = df.groupby("bhk_count")["price"].mean().idxmax() 
# print(f"most_expensive_bhk is {most_expensive_bhk} BHK configuration")

#Question 8 Which property type is the costliest?
most_expensive_property_type = df.groupby('property_type')['price'].max().sort_values(ascending=False).head(1)
# print(most_expensive_property_type)

#Question 9: Do certain builders price higher?
builders_price = df.groupby('company_name')['price'].mean().sort_values(ascending=False)
# print(builders_price)


#Question 10: Are larger homes more expensive per sqft?

sns.scatterplot(data = df , x = 'area', y = 'rate_per_sqft')
# plt.show()