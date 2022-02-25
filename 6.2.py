# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:49:38 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')

def add_10(n):
    return n + 10

df_map = df.applymap(add_10)
print(df_map.head())