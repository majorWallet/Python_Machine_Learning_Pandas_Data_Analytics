# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:35:13 2022

@author: bl4an
"""

import pandas as pd

df1 = pd.read_excel('./남북한발전전력량.xlsx')
df2 = pd.read_excel('./남북한발전전력량.xlsx', header = None)

print(df1)
print()
print(df2)