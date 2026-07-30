import pandas as pd
import numpy as np

#DATAFRAME CONVERTS DATA INTO TABULAR FORM (ROWS AND COLUMNS)

#1st converting np.array into dataframe
array = np.array([["deepak",344,57],["rahul",440,81],["nikhil",453,79]])
#TOTAL PARAMETER DATAFRAME TAKES BUT ALL ARE USED IN REQUIRED SENARIOS.👇
# class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)[source]
df = pd.DataFrame(data = array,columns=["name","total_marks","percentage"])
# print(df)

#2nd converting dictionary into dataframe
dictionary = {"name":["deepak","Dev","shashank","rudra"],"class":[10,12,13,9]}
df1=pd.DataFrame(dictionary)
# print(df1)

# after creating dataframe we get lots of method to perform operations on data..
#examples
#will print first 5 data
df.head()
#will print last 5 data
df.tail()
# provide information about table(dataframe)
df.info()
#similarly
df.describe() #  tells counts,min,max,mean,std


