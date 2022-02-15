# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:21:42 2022

@author: bl4an
"""

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.count())
print()

print(type(df.count()))

unique_values = df['origin'].value_counts()
print(unique_values)
print()
print(type(unique_values))