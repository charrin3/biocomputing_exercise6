#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:47:25 2018

@author: charrington
"""

#code that replicates the functionality of head
def head(x,z):
    filedesired=open(x)
    linenumber=0
    for l in filedesired: 
        linenumber=linenumber+1
        if linenumber > z:
            break
        print l
        
head ("wages.csv",4)

#iris.csv file
import pandas
iris=pandas.read_csv("iris.csv")

#print the last 2 rows and the last two columns in the terminal
row_column=iris.iloc[148:150,3:5]
print(row_column)

#get the number of observations for each species in the set
observations=iris['Species'].value_counts()
print(observations)

#get rows with sepal.width > 3.5
sepalwidth=iris[iris['Sepal.Width']>3.5]
print(sepalwidth)

#write the data for the species setosa to a column delimited file
setosadf=iris[iris['Species']=="setosa"]
setosadf.to_csv('setosa.csv')

#calculate the mean, min, max petal length from virginia
virginica=iris[iris['Species']=="virginica"]
mean=virginica.loc[:,"Petal.Length"].mean()
min=virginica.loc[:,"Petal.Length"].min()
max=virginica.loc[:,"Petal.Length"].max()


