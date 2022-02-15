# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:50:50 2022

@author: bl4an
"""

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
print()
print(type(df))
print()

addition = df + 10
print(addition.tail())
print()
print(type(addition))
print()

subtraction = addition - df
print(subtraction.tail())
print()
print(type(subtraction))