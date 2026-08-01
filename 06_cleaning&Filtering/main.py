import pandas as pd

df = pd.DataFrame({
    "Product_Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": [499, 799, 1199, 899, None] * 200,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes ", " no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})


#SELECTING DATA

#Suppose u want to see only perticular columns

edited_df = df[["Product_Name","price"]]
# print(edited_df)


#FILTERING DATA

#filtering based on single column
filtering_based_on_price = df[df['price'] > 500]
# print(filtering_based_on_price)

#filtering based on multiple columns
fitering = (df['price']>500) & (df['reviews']>600)
# print(df[fitering])

#CLEANING DATA (HANDLING MISSING VALUES)
df.isna() #will give columns with rows true means there is NA in the row and FALSE where there is a value.

df.isna().sum() # it gives a output as collective results for columns where there is a NA in rows
#OUTPUT:
# Product_Name    200 NA PRODUCT NAME IN PRODUCT COLUMN
# price           200
# category        200
# rating          200
# reviews           0
# in_stock        200
# launch_year     200

df.dropna() # will drop all the row which contains none/NA values and give consistent rows only as result.

#FILLING MISSING VALUES

#filling column values
df["rating"] = df['rating'].fillna(df['rating'].mean()) #where i am inserting the mean value of rating column , u can also put manuam value in fillna(anyvalue).

# HANDLING INCINSISTENT MISSING VALUES
df = df.replace(["-", "none", "NULL", "?", "N/A"],'NA') #converts all the types of empty representation symbol into consistent one single symbol.


#changing column datatype
print(df.dtypes)
df["price"] = df["price"].astype(float)
print(df.dtypes)

#renaming column

df.rename(columns={"Product_Name": "Products"}, inplace=True) #here in columns we used {} bracket as we have to change the name in a object style
print(df.dtypes)

#REMOVING DUBLICATES
df.drop_duplicates() #it will remove all dublicates values from the records

#BASIC STRING CLEANING
df["category"] = df["category"].str.lower().str.strip() #strip removes spaces   
#it will create consitent value in the category record

# as u can see ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] these are previous value in categories
# after cleaning  ["mobile", " mobile ", "electronics", "electronics", None]