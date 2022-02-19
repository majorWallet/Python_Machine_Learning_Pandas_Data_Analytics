# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:11:56 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_csv('stock-data.csv')

print(df.head())
print('\n')
print(df.info())

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))

df.set_index('new_Date', inplace = True)
df.drop('Date', axis = 1, inplace = True)

print(df.head())
print('\n')
print(df.info())