#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:47:25 2018

@author: charrington
"""

#code that replicates the functionality of head
import pandas
wages=pandas.read_csv("wages.csv")

head10=wages.head(n=10)

#iris.csv file
iris=pandas.read_csv("iris.csv")

#print the last 2 rows and the last two columns in the terminal
row_column=iris.iloc[148:150,3:5]
print(row_column)

#get the number of observations for each species in the set

#get rows with sepal.width > 3.5
sepalwidth=iris[iris['Sepal.Width']>3.5]

#write the data for the species setosa to a column delimited file
setosa=iris[iris['Species']=="setosa"]

#calculate the mean, min, max petal length from virginia
virginica=iris[iris['Species']=="virginica"]
mean=virginica.loc[:,"Petal.Length"].mean()
min=virginica.loc[:,"Petal.Length"].min()
max=virginica.loc[:,"Petal.Length"].max()


