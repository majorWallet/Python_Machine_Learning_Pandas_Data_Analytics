# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:25:54 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())
print('\n')

def add_two_obj(a, b):
    return a + b

df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis = 1)
print(df.head())