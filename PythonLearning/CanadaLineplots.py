from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df_can = pd.read_excel(r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\Canada.xlsx", sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
print(df_can.head())
#remove unneccasary columns
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df_can.head(2))
#Rename columns so they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.head(2))
#add Total column to sum up total immigrants by country over entire period
df_can['Total'] = df_can.sum(axis=1)
print(df_can.head())
#Check how many null objects we have in the dataset
#print(df_can.isnull().sum())
#Quick summary of each column in the dataframe
print(df_can.describe())

#Now lets try filtering on the list of countries
print(df_can.Country) #returns a series
print(df_can[['Country', 1980, 1982, 1982, 1983, 1984, 1985]]) #returns a dataframe
#Ways to select rows
#df.loc[label] filters by the labels of the index/column
#df.iloc[index] filters by the positions of the index/column
#Notice the default index of the dataset is a numeric range from 0-194, makes it hard to query japan, Fix with set_index()
df_can.set_index('Country', inplace=True)
#And the opposite of set is reset to go back
print(df_can.head())
#remove name of index
#df_can.index.name = None
#print(df_can.head())
print(df_can.loc['Japan'])
#Can also be done by
#print(df_can.iloc[87])
#print(df_can[df_can.index == 'Japan'].T.squeeze())
#can turn columns that are titled with numbers into strings
df_can.columns = list(map(str, df_can.columns))
[print (type(x)) for x in df_can.columns.values] # check type of column
#now that the years are strings lets declare a variable to allow us easily call the full range of years
#useful for ploting later on
years = list(map(str, range(1980,2014)))
print(years)
#you can create a condition booLean series
condition = df_can['Continent'] == 'Asia'
#print(condition)
#then pass condition into the dataframe
print(df_can[condition])
#can also pass multiple criteria in the same line
print(df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')])
#remeber pandas requires & and / instead of and and or
#Now we want to plot Haiti immigrants
haiti = df_can.loc['Haiti', years] # passing in years to exclude the total column
print(haiti.head())
#Years were not displayed because they are of type string
haiti.index = haiti.index.map(int) # change index value of Haiti to int
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
#We can also annotate the peak showing the 2010 earthquake
#syntax: plt.text(x, y, Label)
plt.text(2000,6000, '2010 Earthquake')
#plt.show()
df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.plot(kind='line')
plt.title('Immigration from India and China')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()
#now say we want to plot the top 5 contributors to immigration
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
#get the top 5 entries
df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose()
print(df_top5)
df_top5.plot(kind='line', figsize=(14, 8)) #pass a tuple (x, y) size
plt.show()

#full list of plot types are:bar-vertical bar|barh-horizontal bar| hist-histogram|
#box-box plot| kde or density - density plot| area-area plot|pie-pie plot|scatter|hexbin
