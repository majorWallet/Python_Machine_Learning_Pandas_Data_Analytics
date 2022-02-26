# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:04:52 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all)
print('\n')

print(type(std_all))
print('\n')

std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))

def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())
print('\n')

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('\n')

agg_sep = grouped.agg({'fare' : ['min', 'max'], 'age' : 'mean'})
print(agg_sep.head())
print('\n')