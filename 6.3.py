# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:07:10 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')

def missing_value(series):
    return series.isnull()

result = df.apply(missing_value, axis = 0)
print(result.head())
print('\n')
print(type(result))