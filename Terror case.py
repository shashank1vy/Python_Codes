# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:18:29 2018

@author: Shashank Semwal
"""
import pandas as pd
import os
import numpy as np
terror=pd.read_csv("terror.csv", encoding = 'latin')

os.getcwd()
os.chdir('C:\\Users\\Shashank\\Documents\\python')
#Q.1)	How many attacks happened in India?
terror[terror.country_txt=='India']['country_txt'].count()

#Q.2)	How many attacks happened in India and upto 3 people were killed? 
terror[(terror.country_txt=='India') & (terror.nkill<=3)]['nkill'].count()

#Extract the city and summary for attacks above
terror[(terror.country_txt=='India') & (terror.nkill<=3)][['city','summary']]

#Q.4)	In a single terror incident in India, find out top 5 cities by number killed
terror[(terror.country_txt=='India')][['nkill','city']].sort_values('nkill',ascending=False).head(5)

#Q.5)	In a single terror incident in India, find out top 5 cities by number killed and wounded 
icas=terror[terror.country_txt=='India'][['city','nkill','nwound']]
icas['kill&wound']=icas.nkill+icas.nwound
icas.sort_values(('kill&wound'),ascending=False)[['city','kill&wound']].head(5)

#How many attacks were successful that were suicide attacks?
terror[(terror.success==1) & (terror.suicide==1)]['country'].count()

#label all the incidents where the number killed was more than 5 as severe. 
terror['SevereCheck']=np.NaN
j=0
for i in [terror.nkill] :
    if i>=5:
        terror.loc[j,'SevereCheck']='Severe'
    else:
        terror.loc[j,'SevereCheck']='Not Severe'
    j=j+1

type([terror.nkill])
) write a function to label an incident that was both successful and suicidal
Q.9)	Create a new category representing if the incident occured in Afghanistan, Pakistan or India as one level of the category and all the other countries as another level
Q.10)	How many incidents happened in Af-Pak-India vs ROW?
Q.11)	List the number of suicides attacks and average kills by Af-Pak-India vs ROW. Rename columns in the output as Average_Kills and Number_Incidents.
