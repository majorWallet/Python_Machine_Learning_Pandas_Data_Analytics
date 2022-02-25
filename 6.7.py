# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:15:52 2022

@author: bl4an
"""

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
print(df, '\n')

columns = list(df.columns.values)
print(columns, '\n')

columns_sorted = sorted(columns)
df_sorted = df[columns_sorted]
print(df_sorted, '\n')

columns_reversed = list(reversed(columns))
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = df[columns_customed]
print(df_customed)