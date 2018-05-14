# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:24:35 2018

@author: Admin
"""
import pandas as pd
import os
import numpy as np
air=pd.read_csv("air.txt", encoding = 'latin')

os.getcwd()
os.chdir('C:\\Users\\Shashank\\Documents\\python')

# 1.	Fetch the observations for 9th day of June
air.query("(Month==6) and (Day==9)")

# 2.	Find Average temperature for the month of June. 
air.groupby('Month').agg({'mean'}).query("(Month==6)").loc[:,'Temp']

# 3.	To which day of June has the least temperature
air[(air.Month==6 & air.Temp== int(air[(air.Month==6)].Temp.agg({'min'})))]


# 4.	Find Maximum Ozone value for the month of May
air.groupby('Month').agg({'max'})


