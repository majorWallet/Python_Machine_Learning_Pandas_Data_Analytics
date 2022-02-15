# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:43:09 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print()
print(type(df))
print()

addition = df + 10
print(addition.head())
print()
print(type(addition))