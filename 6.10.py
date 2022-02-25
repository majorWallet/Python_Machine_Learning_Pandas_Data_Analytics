# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:53:43 2022

@author: bl4an
"""

import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 10)

mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())

isin_filter = titanic['sibsp'].isin([3,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())