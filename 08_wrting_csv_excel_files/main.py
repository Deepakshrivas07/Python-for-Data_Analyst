import pandas as pd
#Customer_Info name of df used below
df = pd.DataFrame({
    "name":["deepak","rahul","dev","nikhil"],
    "age":[23,22,31,13]
})
# PRODUCT_SALES name of df used below
df2 = pd.DataFrame({
    "product":["nivia","vivo","smart watch","powder"],
    "sales":[23424,22412,38351,19543]
})
# CREATING AND WRITING .csv, .xlsx files
#.csv
df.to_csv('ecommerce.csv',index = False)
#.xlsx
df.to_excel('ecommerce.xlsx',index = False)

#WRITING MULTIPLE SHEET TO EXCEL
with pd.ExcelWriter('ecommerce.xlsx') as writer:
    df.to_excel(writer,sheet_name='Customer_Info',index=False)
    df2.to_excel(writer,sheet_name='Product_Sales',index=False)


# MORE PARAMETER .csv or.excel takes

df.to_csv('ecommerce_orders',mode='a',header=False,index =False)
#mode = a means APPEND
#header = false means ignore header it is useful when u are appending data
#index = false because excel automatically gives index

# NOTE ALWAYS REMEMBER DO CLEANING AND FILTERING IN PYTHON ONLY DON'T DO IT ON EXCEL.
# NOTE TAKE HELP OF AI