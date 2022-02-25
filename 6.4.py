# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:20:02 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')

def min_max(x):
    return x.max() - x.min()

result = df.apply(min_max)
print(result)
print('\n')
print(type(result))