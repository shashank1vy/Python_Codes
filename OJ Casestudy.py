# -*- coding: utf-8 -*-
"""
Created on Mon May 14 23:42:49 2018

@author: Admin
"""

import pandas as pd
oj=pd.read_csv("C:/Users/Shashank/Desktop/python material/Python Assignments/DataSets/oj.csv")

oj=pd.DataFrame(oj)

# Dimension
oj.shape

# Structure of Dateframe
print(oj.describe)

#Column names in Dataset
print(oj.columns)

#featch first 3 rows of dataset
oj.head(3)

#featch first 1,2,3 columns of dataset
oj.iloc[:,[1,2,3]]

#3.	Fetch the 1,2,8,456th rows of the 1,3,6 columns of the data frame

oj.iloc[[1,2,8,456],[1,3,6]]

# 4.	Fetch the top 5 rows of the brand column
(oj.loc[:,['brand']]).head(5)

# 5.	Fetch top 5 rows of the brand, week and feat details
(oj.loc[:,['brand','week','feat']]).head(5)

# 6.	Fetch the details of all distinct stores
oj.store.unique()

#7.	Fetch all the observations for Tropicana brand
oj[oj['brand']=='tropicana']

# 8. using query function
oj.query("(brand=='tropicana')")

# 9.Fetch bottom 5 observations for those who have bought Tropicana or dominics

(oj.query("(brand=='tropicana') & (brand=='dominicks')")).tail(5)

# groupby and aggregate function
oj.groupby("brand").agg({'price':'mean'})

# 10.	Fetch the income, brand, price observations with Tropicana brand without feature advertisement
oj.query("(feat==0)").loc[:,['income','brand','price']]

# 11.Add a new column in the dataset: logInc which is the logarithm of the income\
oj['logincome']=np.log(oj.loc[:,['INCOME']])

# 12.	Sort the Data in the increasing order of the week

oj.sort_values(axis=0,ascending=True)
sort_value()

oj.sort_values()
sorted(oj,key='week',reverse=True)
oj[oj['feat' == 0]].brand
