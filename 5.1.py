# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:44:20 2022

@author: bl4an
"""

import seaborn as sns
df = sns.load_dataset('titanic')

nan_deck = df['deck'].value_counts(dropna = False)
print(nan_deck)
print(df.head().isnull())
print(df.head().notnull())
print(df.isnull().sum(axis=0))