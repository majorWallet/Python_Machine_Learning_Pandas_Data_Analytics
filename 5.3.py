# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:41:35 2022

@author: bl4an
"""

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['age'].head(10))
print('\n')

mean_age = df['age'].mean(axis = 0)
df['age'].fillna(mean_age, inplace = True)

print(df['age'].head(10))