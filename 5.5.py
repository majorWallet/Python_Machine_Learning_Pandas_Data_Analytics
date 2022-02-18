# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:55:36 2022

@author: bl4an
"""

import seaborn as sns
df = sns.load_dataset('titanic')

print(df['embark_town'][825:830])
print('\n')

df['embark_town'].fillna(method = 'ffill', inplace = True)
print(df['embark_town'][825:830])