import pandas as pd

# READING CSV(.csv)

#read csv files as what is written in file
df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv')

#suppose u have highlighted topic and it contains 2 Rows in csv file and u want to skip it for analysis then,
df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv',skiprows=2)
#Handling missing or broken values (na-values makes missing values consitent in records by giving NAN as result in missing values)
df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv',skiprows=2,na_values=["none","NA","-"])
print(df)

#SEPERATORS {NOTE: The default separator is already a comma, so writing sep="," is optional.}
#if your csv file contains some else sperators like ;,:,|\t then u have to mention it when u read a .csv file
#example 👇
# df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv',skiprows=2,sep=':')

# NOTE SETTING  COLUMN DATATYPES WHILE READING (AS SOME TIME SOFTWARE CAN MISSUNDERSTUD THE DATATYPES SO JUST CALAFIY IT.)
df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv',dtype={"city":str,"rating":int})

#READING LARGE FILE SAFELY BY DIVING IT INTO CHUNKS
df = pd.read_csv('07_read_csv_&_ExcelFile/data.csv',chunksize=10000) #this reads file in smaller pieces

# READING EXCEL(.xlsx)

df2 = pd.read_excel('07_read_csv_&_ExcelFile/Random Data Generator.xlsx')
# print(df2)
# But Excel files often contain multiple sheets, so to Read a specific sheet:
df2 = pd.read_excel('07_read_csv_&_ExcelFile/Random Data Generator.xlsx',sheet_name="Sheet1")


# List all sheet names:
ListAllSheet = pd.ExcelFile('07_read_csv_&_ExcelFile/Random Data Generator.xlsx').sheet_names
# print(ListAllSheet)

